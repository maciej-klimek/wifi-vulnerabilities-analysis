# testcases/reconnect.py

import time
from dependencies.libwifi.wifi import *
from library.testcase import Trigger, Action, Test


class ReconnectTest(Test):
    """Connect → wait → disconnect → wait → reconnect → finish."""
    name = "reconnect"
    kind = Test.Supplicant

    def __init__(self):
        super().__init__([
            # After the *first* connection → run first function
            Action(trigger=Trigger.Connected, action=Action.Function),

            # After the *first* disconnection → run function
            Action(trigger=Trigger.Disconnected, action=Action.Function),

            # After the *second* connection → finish test
            Action(trigger=Trigger.Connected, action=Action.Function),
        ])

    # -----------------------------------------------------------

    def after_first_connect(self, station):
        log(STATUS, "Connected. Waiting 3 seconds before DISCONNECT.")
        time.sleep(3)
        log(STATUS, "Sending DISCONNECT...")
        station.wpaspy_command("DISCONNECT")

    # -----------------------------------------------------------

    def after_first_disconnect(self, station):
        log(STATUS, "Disconnected. Waiting 3 seconds before RECONNECT.")
        time.sleep(3)
        log(STATUS, "Sending RECONNECT...")
        station.wpaspy_command("RECONNECT")

    # -----------------------------------------------------------

    def after_second_connect(self, station):
        log(STATUS, "Reconnected successfully! Waiting 2 seconds before ending...")
        time.sleep(2)
        log(SUCCESS, "Test completed successfully.")
        self.terminate()

    # -----------------------------------------------------------

    def generate(self, station):
        # Assign actions to functions
        self.actions[0].set_function(self.after_first_connect)
        self.actions[1].set_function(self.after_first_disconnect)
        self.actions[2].set_function(self.after_second_connect)
