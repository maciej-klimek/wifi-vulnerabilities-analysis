[20:31:02] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlo1 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlo1: SME: Trying to authenticate with e4:c0:e2:8e:e4:b0 (SSID='PowinnoSmigac' freq=5500 MHz)
wlo1: SME: Trying to authenticate with e4:c0:e2:8e:e4:b0 (SSID='PowinnoSmigac' freq=5500 MHz)
wlo1: PMKSA-CACHE-ADDED e4:c0:e2:8e:e4:b0 0
wlo1: Trying to associate with e4:c0:e2:8e:e4:b0 (SSID='PowinnoSmigac' freq=5500 MHz)
wlo1: Associated with e4:c0:e2:8e:e4:b0
wlo1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlo1: WPA: Key negotiation completed with e4:c0:e2:8e:e4:b0 [PTK=CCMP GTK=CCMP]
wlo1: CTRL-EVENT-CONNECTED - Connection to e4:c0:e2:8e:e4:b0 completed [id=0 id_str=]
[20:31:04] Loaded pairwise and group encryption keys.
[20:31:04] Trigger = Connected.
[20:31:04] Generating queue-saquery-custom test case.
[20:31:05] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=e4:c0:e2:8e:e4:b0 (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=e4:c0:e2:8e:e4:b0 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'PowinnoSmigac' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[20:31:07] Injected <Dot11  subtype=Association Request type=Management addr1=e4:c0:e2:8e:e4:b0 (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=e4:c0:e2:8e:e4:b0 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'PowinnoSmigac' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
^CTraceback (most recent call last):
  File "/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/./run.py", line 78, in <module>
p2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
p2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
    station.run()
nl80211: deinit ifname=p2p-dev-wlo1 disabled_11b_rates=0
  File "/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/library/daemon.py", line 220, in run
    sel = select.select(sockets, [], [], 0.5)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
[20:32:04] Closing daemon and cleaning up ...
p2p-dev-wlo1: CTRL-EVENT-TERMINATING 
wlo1: CTRL-EVENT-DISCONNECTED bssid=e4:c0:e2:8e:e4:b0 reason=3 locally_generated=1
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
wlo1: PMKSA-CACHE-REMOVED e4:c0:e2:8e:e4:b0 0
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlo1 disabled_11b_rates=0
wlo1: CTRL-EVENT-TERMINATING 


> stuck at 2nd inject


## !! ramki do przeglądnięcia - endeless action exchange (sa query? encrypted?)