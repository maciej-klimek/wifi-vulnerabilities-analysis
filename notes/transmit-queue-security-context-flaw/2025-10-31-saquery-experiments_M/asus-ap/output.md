(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework# ./run.py wlo1 queue-saquery-asus
[14:14:11] Using interface monwlo1 (iwlwifi) to inject frames.
[14:14:11] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlo1 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlo1: SME: Trying to authenticate with c8:7f:54:bf:0d:74 (SSID='testnetwork-asus' freq=2412 MHz)
wlo1: SME: Trying to authenticate with c8:7f:54:bf:0d:74 (SSID='testnetwork-asus' freq=2412 MHz)
wlo1: PMKSA-CACHE-ADDED c8:7f:54:bf:0d:74 0
wlo1: Trying to associate with c8:7f:54:bf:0d:74 (SSID='testnetwork-asus' freq=2412 MHz)
wlo1: Associated with c8:7f:54:bf:0d:74
wlo1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlo1: WPA: Key negotiation completed with c8:7f:54:bf:0d:74 [PTK=CCMP GTK=CCMP]
wlo1: CTRL-EVENT-CONNECTED - Connection to c8:7f:54:bf:0d:74 completed [id=0 id_str=]
[14:14:14] Loaded pairwise and group encryption keys.
[14:14:14] Trigger = Connected.
[14:14:14] Generating queue-saquery-asus test case.
[14:14:15] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=c8:7f:54:bf:0d:74 (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=c8:7f:54:bf:0d:74 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-motorola' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[14:14:17] Injected <Dot11  subtype=Association Request type=Management addr1=c8:7f:54:bf:0d:74 (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=c8:7f:54:bf:0d:74 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-motorola' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
^CTraceback (most recent call last):