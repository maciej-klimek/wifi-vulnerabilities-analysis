## Client/Testcase

(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework# ./run.py wlo1 queue-saquery-samsung
[22:18:13] Using interface monwlo1 (iwlwifi) to inject frames.
[22:18:13] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlo1 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlo1: SME: Trying to authenticate with 06:86:f4:50:c8:18 (SSID='testnetwork-samsung' freq=2412 MHz)
wlo1: SME: Trying to authenticate with 06:86:f4:50:c8:18 (SSID='testnetwork-samsung' freq=2412 MHz)
wlo1: PMKSA-CACHE-ADDED 06:86:f4:50:c8:18 0
wlo1: Trying to associate with 06:86:f4:50:c8:18 (SSID='testnetwork-samsung' freq=2412 MHz)
wlo1: Associated with 06:86:f4:50:c8:18
wlo1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlo1: WPA: Key negotiation completed with 06:86:f4:50:c8:18 [PTK=CCMP GTK=CCMP]
wlo1: CTRL-EVENT-CONNECTED - Connection to 06:86:f4:50:c8:18 completed [id=0 id_str=]
[22:18:15] Loaded pairwise and group encryption keys.
[22:18:15] Trigger = Connected.
[22:18:15] Generating queue-saquery-samsung test case.
[22:18:16] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=06:86:f4:50:c8:18 (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=06:86:f4:50:c8:18 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-samsung' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[22:18:18] Injected <Dot11  subtype=Association Request type=Management addr1=06:86:f4:50:c8:18 (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=06:86:f4:50:c8:18 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-samsung' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[22:18:18] 802.11 Management Deauthentication 06:86:f4:50:c8:18 (TA=SA) > a0:51:0b:65:8e:70 (RA=DA) / Dot11Deauth
[22:18:18] Detected an unprotected deauthentication frame from AP.
[22:18:18] Trigger = Received.
[22:18:20] Disconnecting.
p2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
[22:18:20] Closing daemon and cleaning up ...
p2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=p2p-dev-wlo1 disabled_11b_rates=0
p2p-dev-wlo1: CTRL-EVENT-TERMINATING 
wlo1: CTRL-EVENT-DISCONNECTED bssid=06:86:f4:50:c8:18 reason=3 locally_generated=1
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
wlo1: PMKSA-CACHE-REMOVED 06:86:f4:50:c8:18 0
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlo1 disabled_11b_rates=0
wlo1: CTRL-EVENT-TERMINATING 


matches the virtual test:)