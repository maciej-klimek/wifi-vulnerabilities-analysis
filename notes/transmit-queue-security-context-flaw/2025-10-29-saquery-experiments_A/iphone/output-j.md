(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework# ./run.py wlo1 queue-saquery-iphone-wpa3
[19:09:23] Using interface monwlo1 (iwlwifi) to inject frames.
[19:09:23] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlo1 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlo1: SME: Trying to authenticate with d6:ab:e3:60:9d:73 (SSID='testnetwork-iphone-J' freq=2437 MHz)
wlo1: SME: Trying to authenticate with d6:ab:e3:60:9d:73 (SSID='testnetwork-iphone-J' freq=2437 MHz)
wlo1: PMKSA-CACHE-ADDED d6:ab:e3:60:9d:73 0
wlo1: Trying to associate with d6:ab:e3:60:9d:73 (SSID='testnetwork-iphone-J' freq=2437 MHz)
wlo1: Associated with d6:ab:e3:60:9d:73
wlo1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlo1: WPA: Key negotiation completed with d6:ab:e3:60:9d:73 [PTK=CCMP GTK=CCMP]
wlo1: CTRL-EVENT-CONNECTED - Connection to d6:ab:e3:60:9d:73 completed [id=0 id_str=]
[19:09:24] Loaded pairwise and group encryption keys.
[19:09:24] Trigger = Connected.
[19:09:24] Generating queue-saquery-iphone-wpa3 test case.
[19:09:25] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=d6:ab:e3:60:9d:73 (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=d6:ab:e3:60:9d:73 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-iphone-J' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[19:09:27] Injected <Dot11  subtype=Association Request type=Management addr1=d6:ab:e3:60:9d:73 (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=d6:ab:e3:60:9d:73 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-iphone-J' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
        ^Cp2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
Traceback (most recent call last):
  File "/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/./run.py", line 78, in <module>
p2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=p2p-dev-wlo1 disabled_11b_rates=0
    station.run()
  File "/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/library/daemon.py", line 220, in run
    sel = select.select(sockets, [], [], 0.5)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
[19:10:39] Closing daemon and cleaning up ...
p2p-dev-wlo1: CTRL-EVENT-TERMINATING 
wlo1: CTRL-EVENT-DISCONNECTED bssid=d6:ab:e3:60:9d:73 reason=3 locally_generated=1
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
wlo1: PMKSA-CACHE-REMOVED d6:ab:e3:60:9d:73 0
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlo1 disabled_11b_rates=0
wlo1: CTRL-EVENT-TERMINATING 

udalo sie odpalic wpa3 - niepodatny 