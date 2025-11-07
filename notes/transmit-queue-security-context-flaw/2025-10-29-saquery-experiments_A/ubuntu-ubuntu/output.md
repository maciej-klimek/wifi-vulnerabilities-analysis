

AP - Adi:
~/Desktop/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework (main*) » sudo "$(which python)" ./hostap.py wlp0s20f3 --ap          atis@atis-Latitude-5420
[18:04:13] Using interface monwlp0s20f3 (iwlwifi) to inject frames.
[18:04:13] Starting daemon using: ./dependencies/hostap_2_10/hostapd/hostapd -i wlp0s20f3 ./setup/hostapd.conf -K
wlp0s20f3: interface state UNINITIALIZED->ENABLED
wlp0s20f3: AP-ENABLED 
wlp0s20f3: AP-STA-ASSOCIATING a0:51:0b:65:8e:70
wlp0s20f3: STA a0:51:0b:65:8e:70 IEEE 802.11: associated (aid 1)
wlp0s20f3: AP-STA-CONNECTED a0:51:0b:65:8e:70
wlp0s20f3: STA a0:51:0b:65:8e:70 RADIUS: starting accounting session 9B0626CFEC5CDC79
wlp0s20f3: STA a0:51:0b:65:8e:70 WPA: pairwise key handshake completed (RSN)
wlp0s20f3: EAPOL-4WAY-HS-COMPLETED a0:51:0b:65:8e:70
wlp0s20f3: AP-STA-DISCONNECTED a0:51:0b:65:8e:70

Suplicant - Martin:
[18:05:58] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlo1 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlo1: CTRL-EVENT-REGDOM-CHANGE init=DRIVER type=COUNTRY alpha2=EU
wlo1: SME: Trying to authenticate with ec:63:d7:89:d5:5a (SSID='testnetwork-ubuntu' freq=2412 MHz)
wlo1: SME: Trying to authenticate with ec:63:d7:89:d5:5a (SSID='testnetwork-ubuntu' freq=2412 MHz)
wlo1: PMKSA-CACHE-ADDED ec:63:d7:89:d5:5a 0
wlo1: Trying to associate with ec:63:d7:89:d5:5a (SSID='testnetwork-ubuntu' freq=2412 MHz)
wlo1: Associated with ec:63:d7:89:d5:5a
wlo1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlo1: WPA: Key negotiation completed with ec:63:d7:89:d5:5a [PTK=CCMP GTK=CCMP]
wlo1: CTRL-EVENT-CONNECTED - Connection to ec:63:d7:89:d5:5a completed [id=0 id_str=]
[18:06:01] Loaded pairwise and group encryption keys.
[18:06:01] Trigger = Connected.
[18:06:01] Generating queue-saquery-ubuntu test case.
[18:06:02] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=ec:63:d7:89:d5:5a (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=ec:63:d7:89:d5:5a (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-ubuntu' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[18:06:04] Injected <Dot11  subtype=Association Request type=Management addr1=ec:63:d7:89:d5:5a (RA=DA) addr2=a0:51:0b:65:8e:70 (TA=SA) addr3=ec:63:d7:89:d5:5a (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-ubuntu' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
^CTraceback (most recent call last):
  File "/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/./run.py", line 78, in <module>
p2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
p2p-dev-wlo1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=p2p-dev-wlo1 disabled_11b_rates=0
    station.run()
  File "/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/library/daemon.py", line 220, in run
    sel = select.select(sockets, [], [], 0.5)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
[18:09:49] Closing daemon and cleaning up ...
p2p-dev-wlo1: CTRL-EVENT-TERMINATING 
wlo1: CTRL-EVENT-DISCONNECTED bssid=ec:63:d7:89:d5:5a reason=3 locally_generated=1
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
wlo1: PMKSA-CACHE-REMOVED ec:63:d7:89:d5:5a 0
wlo1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlo1 disabled_11b_rates=0
wlo1: CTRL-EVENT-TERMINATING 



Supplicant Adi :
~/Desktop/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework (main) » sudo "$(which python)" ./run.py wlp0s20f3 queue-saquery-ubuntu             
[18:29:54] Using interface monwlp0s20f3 (iwlwifi) to inject frames.
[18:29:54] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlp0s20f3 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
wlp0s20f3: SME: Trying to authenticate with a0:51:0b:65:8e:70 (SSID='testnetwork-ubuntu' freq=2412 MHz)
wlp0s20f3: SME: Trying to authenticate with a0:51:0b:65:8e:70 (SSID='testnetwork-ubuntu' freq=2412 MHz)
wlp0s20f3: PMKSA-CACHE-ADDED a0:51:0b:65:8e:70 0
wlp0s20f3: Trying to associate with a0:51:0b:65:8e:70 (SSID='testnetwork-ubuntu' freq=2412 MHz)
wlp0s20f3: Associated with a0:51:0b:65:8e:70
wlp0s20f3: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlp0s20f3: WPA: Key negotiation completed with a0:51:0b:65:8e:70 [PTK=CCMP GTK=CCMP]
wlp0s20f3: CTRL-EVENT-CONNECTED - Connection to a0:51:0b:65:8e:70 completed [id=0 id_str=]
[18:29:56] Loaded pairwise and group encryption keys.
[18:29:56] Trigger = Connected.
[18:29:56] Generating queue-saquery-ubuntu test case.
[18:29:57] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=a0:51:0b:65:8e:70 (RA=DA) addr2=ec:63:d7:89:d5:5a (TA=SA) addr3=a0:51:0b:65:8e:70 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-ubuntu' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[18:29:59] Injected <Dot11  subtype=Association Request type=Management addr1=a0:51:0b:65:8e:70 (RA=DA) addr2=ec:63:d7:89:d5:5a (TA=SA) addr3=a0:51:0b:65:8e:70 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-ubuntu' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>