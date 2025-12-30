~/Desktop/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework (main*) » sudo "$(which python)" ./run.py wlp0s20f3 queue-saquery-iphone     atis@atis-Latitude-5420
[18:50:50] Using interface monwlp0s20f3 (iwlwifi) to inject frames.
[18:50:50] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlp0s20f3 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlp0s20f3: SME: Trying to authenticate with 5e:1d:1c:09:de:2c (SSID='iPhoneAdrian' freq=2437 MHz)
wlp0s20f3: Trying to associate with 5e:1d:1c:09:de:2c (SSID='iPhoneAdrian' freq=2437 MHz)
wlp0s20f3: Associated with 5e:1d:1c:09:de:2c
wlp0s20f3: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlp0s20f3: WPA: Key negotiation completed with 5e:1d:1c:09:de:2c [PTK=CCMP GTK=CCMP]
wlp0s20f3: CTRL-EVENT-CONNECTED - Connection to 5e:1d:1c:09:de:2c completed [id=0 id_str=]
[18:50:53] Loaded pairwise and group encryption keys.
[18:50:53] Trigger = Connected.
[18:50:53] Generating queue-saquery-iphone test case.
[18:50:54] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=5e:1d:1c:09:de:2c (RA=DA) addr2=ec:63:d7:89:d5:5a (TA=SA) addr3=5e:1d:1c:09:de:2c (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'iPhone (Adrian)' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[18:50:56] Injected <Dot11  subtype=Association Request type=Management addr1=5e:1d:1c:09:de:2c (RA=DA) addr2=ec:63:d7:89:d5:5a (TA=SA) addr3=5e:1d:1c:09:de:2c (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'iPhone (Adrian)' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
^CTraceback (most recent call last):
  File "./run.py", line 78, in <module>
p2p-dev-wlp0s20: CTRL-EVENT-DSCP-POLICY clear_all
p2p-dev-wlp0s20: CTRL-EVENT-DSCP-POLICY clear_all
    station.run()
  File "/home/atis/Desktop/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/library/daemon.py", line 220, in run
nl80211: deinit ifname=p2p-dev-wlp0s20 disabled_11b_rates=0
    sel = select.select(sockets, [], [], 0.5)
KeyboardInterrupt
[18:51:33] Closing daemon and cleaning up ...
p2p-dev-wlp0s20: CTRL-EVENT-TERMINATING 
wlp0s20f3: CTRL-EVENT-DISCONNECTED bssid=5e:1d:1c:09:de:2c reason=3 locally_generated=1
wlp0s20f3: CTRL-EVENT-DSCP-POLICY clear_all
wlp0s20f3: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlp0s20f3 disabled_11b_rates=0
wlp0s20f3: CTRL-EVENT-TERMINATING 