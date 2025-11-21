from scapy.all import *

INTERFACE = "monwlan1"
AP_MAC = "02:00:00:00:00:00"
CLIENT_MAC = "02:00:00:00:01:00"
SSID = "testnetwork"


# === Helper Functions ===

def build_auth_request():
    """Builds an Authentication Request (Open System - algo 0)."""
    dot11 = Dot11(
        type=0, subtype=11,
        addr1=AP_MAC, addr2=CLIENT_MAC, addr3=AP_MAC
    )
    auth_req = Dot11Auth(algo=0, seqnum=1, status=0)
    return RadioTap() / dot11 / auth_req


def build_assoc_request():
    """Builds an Association Request for WPA3 (PMF) z POPRAWNYM RSN IE."""
    dot11 = Dot11(
        type=0, subtype=0,
        addr1=AP_MAC, addr2=CLIENT_MAC, addr3=AP_MAC
    )
    # cap=0x1031: PMF Required
    assoc_req = Dot11AssoReq(cap=0x1031, listen_interval=1)

    # RSN IE (POPRAWIONY)
    rsn_info = (
        b'\x01\x00' +                 # Version
        b'\x00\x0f\ac\x04' +         # Group Cipher: CCMP-128
        b'\x01\x00' +                 # Pairwise Cipher Count
        b'\x00\x0f\ac\x04' +         # Pairwise Cipher: CCMP-128
        b'\x01\x00' +                 # AKM Count
        # AKM: SAE (WPA3-Personal) <--- PRAWIDŁOWY AKM
        b'\x00\x0f\ac\x08' +
        b'\x00\x80'                   # RSN Capabilities: PMF Required
    )

    # HT Capabilities ma ID = 45 (0x2d)
    ht_cap_info = b'\x6f\x01\x17\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    elements = (
        # ID=0 (SSID)
        Dot11Elt(ID=0, info=SSID) /
        # ID=1 (Supported Rates)
        Dot11Elt(ID=1, info=b'\x82\x04\x8b\x96\x0c\x18\x30\x48') /
        # ID=48 (RSNinfo)
        Dot11Elt(ID=48, info=rsn_info) /
        # ID=45 (HT Cap)
        Dot11Elt(ID=45, info=ht_cap_info)
    )
    return RadioTap() / dot11 / assoc_req / elements


# === Main Logic ===

def complete_connection_and_listen():
    """Runs the connection steps and listens for EAPOL Msg 1."""

    print(f"Starting connection process on interface: {INTERFACE}")
    print(f"   AP (BSSID): {AP_MAC}, Client (STA): {CLIENT_MAC}, SSID: {SSID}")

    # 1. Probe Request
    print("\n[1] SENDING: Probe Request...")
    sendp(RadioTap()/Dot11(type=0, subtype=4, addr1="ff:ff:ff:ff:ff:ff", addr2=CLIENT_MAC,
          addr3="ff:ff:ff:ff:ff:ff")/Dot11ProbeReq()/Dot11Elt(ID=0, info=SSID), iface=INTERFACE, verbose=False)

    # 2. Authentication (Open System)
    print("[2] SENDING: Authentication Request (Open System)...")
    sendp(build_auth_request(), iface=INTERFACE, verbose=False)

    # Czekamy na odpowiedź Auth (seqnum=2, status=0)
    auth_resp = sniff(iface=INTERFACE, lfilter=lambda x: x.haslayer(
        Dot11Auth) and x.addr2 == AP_MAC and x[Dot11Auth].seqnum == 2 and x[Dot11Auth].status == 0, timeout=1, count=1)

    if auth_resp:
        print("Authentication successful (Status 0).")
    else:
        print("Authentication failed or timeout. Continuing to Association...")

    # 3. Association Request
    print("[3] SENDING: Association Request (WPA3 RSN IE)...")
    sendp(build_assoc_request(), iface=INTERFACE, verbose=False)

    # Czekamy na odpowiedź Assoc (status=0)
    assoc_resp = sniff(iface=INTERFACE, lfilter=lambda x: x.haslayer(
        Dot11AssoResp) and x.addr2 == AP_MAC and x[Dot11AssoResp].status == 0, timeout=1, count=1)

    if assoc_resp:
        print("Association successful (Status 0). Client is ASSOCIATED.")
    else:
        print("Association failed or timeout. AP likely requires SAE.")
        print("   Checking if AP starts 4WH mimo nieudanego skojarzenia...")

    print("--- AP should now be attempting 4-way Handshake ---")

    # 4. Listen for EAPOL Key Msg 1 (CZY AP WYSŁAŁ PIERWSZĄ WIADOMOŚĆ)
    print("\n[4] LISTENING: Waiting for EAPOL Key Msg 1 (10s timeout)...")

    eapol_msg1_list = sniff(iface=INTERFACE, lfilter=lambda x: x.haslayer(
        EAPOL) and x.addr2 == AP_MAC, timeout=10, count=1)

    if eapol_msg1_list:
        print("SUCCESS! Received EAPOL Key Msg 1.")
        print("   Hostapd successfully started the 4-way Handshake.")
    else:
        print("FAILURE. Did NOT receive EAPOL Key Msg 1 (Timeout).")
        print("   AP odrzucił połączenie przed rozpoczęciem 4WH (prawdopodobnie przez wymóg SAE).")


if __name__ == "__main__":
    try:
        complete_connection_and_listen()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
