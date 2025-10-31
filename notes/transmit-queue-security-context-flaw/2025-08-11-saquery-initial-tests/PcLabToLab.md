(base) student@ubuntu:~/Desktop/wifi-framework$ sudo ./run.py wlp6s0 queue-saquery
[11:22:38] Using interface monwlp6s0 (ath9k) to inject frames.
[11:22:38] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlp6s0 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlp6s0: SME: Trying to authenticate with 30:b5:c2:67:a4:32 (SSID='testnetwork' freq=2412 MHz)
wlp6s0: SME: Trying to authenticate with 30:b5:c2:67:a4:32 (SSID='testnetwork' freq=2412 MHz)
wlp6s0: PMKSA-CACHE-ADDED 30:b5:c2:67:a4:32 0
wlp6s0: Trying to associate with 30:b5:c2:67:a4:32 (SSID='testnetwork' freq=2412 MHz)
wlp6s0: Associated with 30:b5:c2:67:a4:32
wlp6s0: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlp6s0: WPA: Key negotiation completed with 30:b5:c2:67:a4:32 [PTK=CCMP GTK=CCMP]
wlp6s0: CTRL-EVENT-CONNECTED - Connection to 30:b5:c2:67:a4:32 completed [id=0 id_str=]
[11:22:40] Loaded pairwise and group encryption keys.
[11:22:40] Trigger = Connected.
[11:22:40] Generating queue-saquery test case.
[11:22:41] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=30:b5:c2:67:a4:32 (RA=DA) addr2=e8:de:27:13:0f:13 (TA=SA) addr3=30:b5:c2:67:a4:32 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[11:22:44] Injected <Dot11  subtype=Association Request type=Management addr1=30:b5:c2:67:a4:32 (RA=DA) addr2=e8:de:27:13:0f:13 (TA=SA) addr3=30:b5:c2:67:a4:32 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[11:22:48] 802.11 Management Deauthentication 30:b5:c2:67:a4:32 (TA=SA) > e8:de:27:13:0f:13 (RA=DA) / Dot11Deauth
[11:22:48] Detected an unprotected deauthentication frame from AP.
[11:22:48] Trigger = Received.
[11:22:50] Disconnecting.
[11:22:50] Closing daemon and cleaning up ...
wlp6s0: CTRL-EVENT-DISCONNECTED bssid=30:b5:c2:67:a4:32 reason=3 locally_generated=1
wlp6s0: CTRL-EVENT-DSCP-POLICY clear_all
wlp6s0: PMKSA-CACHE-REMOVED 30:b5:c2:67:a4:32 0
wlp6s0: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlp6s0 disabled_11b_rates=0
wlp6s0: CTRL-EVENT-TERMINATING 


w drugą strone :)

sudo ./run.py wlp5s0 queue-saquery
[11:25:05] Using interface monwlp5s0 (ath9k) to inject frames.
[11:25:05] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlp5s0 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlp5s0: SME: Trying to authenticate with e8:de:27:13:0f:13 (SSID='testnetwork' freq=2412 MHz)
wlp5s0: SME: Trying to authenticate with e8:de:27:13:0f:13 (SSID='testnetwork' freq=2412 MHz)
wlp5s0: PMKSA-CACHE-ADDED e8:de:27:13:0f:13 0
wlp5s0: Trying to associate with e8:de:27:13:0f:13 (SSID='testnetwork' freq=2412 MHz)
wlp5s0: Associated with e8:de:27:13:0f:13
wlp5s0: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlp5s0: WPA: Key negotiation completed with e8:de:27:13:0f:13 [PTK=CCMP GTK=CCMP]
wlp5s0: CTRL-EVENT-CONNECTED - Connection to e8:de:27:13:0f:13 completed [id=0 id_str=]
[11:25:06] Loaded pairwise and group encryption keys.
[11:25:06] Trigger = Connected.
[11:25:06] Generating queue-saquery test case.
[11:25:07] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=e8:de:27:13:0f:13 (RA=DA) addr2=30:b5:c2:67:a4:32 (TA=SA) addr3=e8:de:27:13:0f:13 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[11:25:09] Injected <Dot11  subtype=Association Request type=Management addr1=e8:de:27:13:0f:13 (RA=DA) addr2=30:b5:c2:67:a4:32 (TA=SA) addr3=e8:de:27:13:0f:13 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[11:25:13] 802.11 Management Deauthentication e8:de:27:13:0f:13 (TA=SA) > 30:b5:c2:67:a4:32 (RA=DA) / Dot11Deauth
[11:25:13] Detected an unprotected deauthentication frame from AP.
[11:25:13] Trigger = Received.
[11:25:15] Disconnecting.
[11:25:15] Closing daemon and cleaning up ...
wlp5s0: CTRL-EVENT-DISCONNECTED bssid=e8:de:27:13:0f:13 reason=3 locally_generated=1
wlp5s0: CTRL-EVENT-DSCP-POLICY clear_all
wlp5s0: PMKSA-CACHE-REMOVED e8:de:27:13:0f:13 0
wlp5s0: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlp5s0 disabled_11b_rates=0
wlp5s0: CTRL-EVENT-TERMINATING 
