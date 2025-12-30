## WPA3:

(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework# ./run.py wlo1 queue-saquery-motorola
[21:33:39] Using interface monwlo1 (iwlwifi) to inject frames.
[21:33:39] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlo1 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlo1: CTRL-EVENT-REGDOM-CHANGE init=DRIVER type=COUNTRY alpha2=PL
wlo1: SME: Trying to authenticate with e2:e1:14:61:35:9f (SSID='testnetwork-motorola' freq=2412 MHz)
wlo1: SME: Trying to authenticate with e2:e1:14:61:35:9f (SSID='testnetwork-motorola' freq=2412 MHz)
wlo1: PMKSA-CACHE-ADDED e2:e1:14:61:35:9f 0
wlo1: Trying to associate with e2:e1:14:61:35:9f (SSID='testnetwork-motorola' freq=2412 MHz)
wlo1: Associated with e2:e1:14:61:35:9f
wlo1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlo1: WPA: Key negotiation completed with e2:e1:14:61:35:9f [PTK=CCMP GTK=CCMP]
wlo1: CTRL-EVENT-CONNECTED - Connection to e2:e1:14:61:35:9f completed [id=0 id_str=]
[21:33:43] Loaded pairwise and group encryption keys.
[21:33:43] Trigger = Connected.
[21:33:43] Generating queue-saquery-motorola test case.
[21:33:44] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=e2:e1:14:61:35:9f (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=e2:e1:14:61:35:9f (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-motorola' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[21:33:46] Injected <Dot11  subtype=Association Request type=Management addr1=e2:e1:14:61:35:9f (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=e2:e1:14:61:35:9f (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-motorola' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
^CTraceback (most recent call last):
p2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
  File "/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/./run.py", line 78, in <module>
p2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
    station.run()
nl80211: deinit ifname=p2p-dev-wlo1 disabled_11b_rates=0
  File "/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/library/daemon.py", line 220, in run
    sel = select.select(sockets, [], [], 0.5)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
[21:34:53] Closing daemon and cleaning up ...
p2p-dev-wlo1: CTRL-EVENT-TERMINATING 
wlo1: CTRL-EVENT-DISCONNECTED bssid=e2:e1:14:61:35:9f reason=3 locally_generated=1
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
wlo1: PMKSA-CACHE-REMOVED e2:e1:14:61:35:9f 0
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlo1 disabled_11b_rates=0
wlo1: CTRL-EVENT-TERMINATING 

> WPA3 bez pmf - tak samo


## WPA2:

(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework# ./run.py wlo1 queue-saquery-motorola
[21:42:52] Using interface monwlo1 (iwlwifi) to inject frames.
[21:42:52] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlo1 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlo1: SME: Trying to authenticate with e2:e1:14:61:35:9f (SSID='testnetwork-motorola' freq=2437 MHz)
wlo1: Trying to associate with e2:e1:14:61:35:9f (SSID='testnetwork-motorola' freq=2437 MHz)
wlo1: Associated with e2:e1:14:61:35:9f
wlo1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlo1: WPA: Key negotiation completed with e2:e1:14:61:35:9f [PTK=CCMP GTK=CCMP]
wlo1: CTRL-EVENT-CONNECTED - Connection to e2:e1:14:61:35:9f completed [id=0 id_str=]
[21:42:55] Loaded pairwise and group encryption keys.
[21:42:55] Trigger = Connected.
[21:42:55] Generating queue-saquery-motorola test case.
[21:42:56] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=e2:e1:14:61:35:9f (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=e2:e1:14:61:35:9f (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-motorola' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[21:42:58] Injected <Dot11  subtype=Association Request type=Management addr1=e2:e1:14:61:35:9f (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=e2:e1:14:61:35:9f (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-motorola' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
^Cp2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
Traceback (most recent call last):
  File "/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/./run.py", line 78, in <module>
    station.run()
p2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=p2p-dev-wlo1 disabled_11b_rates=0
  File "/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/library/daemon.py", line 220, in run
    sel = select.select(sockets, [], [], 0.5)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
[21:44:28] Closing daemon and cleaning up ...
p2p-dev-wlo1: CTRL-EVENT-TERMINATING 
wlo1: CTRL-EVENT-DISCONNECTED bssid=e2:e1:14:61:35:9f reason=3 locally_generated=1
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlo1 disabled_11b_rates=0
wlo1: CTRL-EVENT-TERMINATING 