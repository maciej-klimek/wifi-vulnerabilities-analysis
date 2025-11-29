(venv) -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Desktop/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework (main*) » sudo systemctl stop NetworkManager                            atis@atis-Latitude-5420
(venv) -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Desktop/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework (main*) » sudo "$(which python)" ./run.py wlp0s20f3 queue-saquery-laura
[22:11:03] Using interface monwlp0s20f3 (iwlwifi) to inject frames.
[22:11:03] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlp0s20f3 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlp0s20f3: SME: Trying to authenticate with fa:12:c2:79:7c:03 (SSID='testnetwork-laura' freq=5220 MHz)
wlp0s20f3: SME: Trying to authenticate with fa:12:c2:79:7c:03 (SSID='testnetwork-laura' freq=5220 MHz)
wlp0s20f3: PMKSA-CACHE-ADDED fa:12:c2:79:7c:03 0
wlp0s20f3: Trying to associate with fa:12:c2:79:7c:03 (SSID='testnetwork-laura' freq=5220 MHz)
wlp0s20f3: Associated with fa:12:c2:79:7c:03
wlp0s20f3: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlp0s20f3: WPA: Key negotiation completed with fa:12:c2:79:7c:03 [PTK=CCMP GTK=CCMP]
wlp0s20f3: CTRL-EVENT-CONNECTED - Connection to fa:12:c2:79:7c:03 completed [id=0 id_str=]
[22:11:05] Loaded pairwise and group encryption keys.
[22:11:05] Trigger = Connected.
[22:11:05] Generating queue-saquery-laura test case.
[22:11:06] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=fa:12:c2:79:7c:03 (RA=DA) addr2=ec:63:d7:89:d5:5a (TA=SA) addr3=fa:12:c2:79:7c:03 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-laura' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[22:11:08] Injected <Dot11  subtype=Association Request type=Management addr1=fa:12:c2:79:7c:03 (RA=DA) addr2=ec:63:d7:89:d5:5a (TA=SA) addr3=fa:12:c2:79:7c:03 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-laura' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
^CTraceback (most recent call last):
  File "./run.py", line 78, in <module>
p2p-dev-wlp0s20: CTRL-EVENT-DSCP-POLICY clear_all
p2p-dev-wlp0s20: CTRL-EVENT-DSCP-POLICY clear_all
    station.run()
nl80211: deinit ifname=p2p-dev-wlp0s20 disabled_11b_rates=0
  File "/home/atis/Desktop/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/library/daemon.py", line 220, in run
    sel = select.select(sockets, [], [], 0.5)
KeyboardInterrupt
[22:11:55] Closing daemon and cleaning up ...
p2p-dev-wlp0s20: CTRL-EVENT-TERMINATING 
wlp0s20f3: CTRL-EVENT-DISCONNECTED bssid=fa:12:c2:79:7c:03 reason=3 locally_generated=1
wlp0s20f3: CTRL-EVENT-DSCP-POLICY clear_all
wlp0s20f3: PMKSA-CACHE-REMOVED fa:12:c2:79:7c:03 0
wlp0s20f3: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlp0s20f3 disabled_11b_rates=0
wlp0s20f3: CTRL-EVENT-TERMINATING 

(venv) ------------------------------------