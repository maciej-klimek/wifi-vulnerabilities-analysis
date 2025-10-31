## Setup:

(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework# cd setup
(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/setup# ./setup-hwsim.sh 4
Created hwsim interface wlan0
Created hwsim interface wlan1
Created hwsim interface wlan2
Created hwsim interface wlan3
(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/setup# ./load-config.sh wpa3-personal-pmf
Loaded hostapd-wpa3-personal-pmf.conf
Loaded supplicant-wpa3-personal-pmf.conf
(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework/setup# cd ..
(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework# 

## AP:
(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework# ./hostap.py wlan0 --ap
[21:59:15] Using interface monwlan0 (mac80211_hwsim) to inject frames.
[21:59:15] Starting daemon using: ./dependencies/hostap_2_10/hostapd/hostapd -i wlan0 ./setup/hostapd.conf -K
wlan0: interface state UNINITIALIZED->ENABLED
wlan0: AP-ENABLED 
wlan0: AP-STA-ASSOCIATING 02:00:00:00:01:00
wlan0: STA 02:00:00:00:01:00 IEEE 802.11: associated (aid 1)
wlan0: AP-STA-CONNECTED 02:00:00:00:01:00
wlan0: STA 02:00:00:00:01:00 RADIUS: starting accounting session F1ABFF22AEE36064
wlan0: STA 02:00:00:00:01:00 WPA: pairwise key handshake completed (RSN)
wlan0: EAPOL-4WAY-HS-COMPLETED 02:00:00:00:01:00
wlan0: AP-STA-ASSOCIATING 02:00:00:00:01:00
wlan0: STA 02:00:00:00:01:00 IEEE 802.11: associated (aid 1)
wlan0: AP-STA-DISCONNECTED 02:00:00:00:01:00
wlan0: STA 02:00:00:00:01:00 IEEE 802.11: deauthenticated due to local deauth request

## Client/Testcase:
(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework# ./run.py wlan1 queue-saquery
[22:02:28] Using interface monwlan1 (mac80211_hwsim) to inject frames.
[22:02:28] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlan1 -c ./setup/supplicant.conf -W -K
wlan1: SME: Trying to authenticate with 02:00:00:00:00:00 (SSID='testnetwork' freq=2412 MHz)
wlan1: SME: Trying to authenticate with 02:00:00:00:00:00 (SSID='testnetwork' freq=2412 MHz)
wlan1: PMKSA-CACHE-ADDED 02:00:00:00:00:00 0
wlan1: Trying to associate with 02:00:00:00:00:00 (SSID='testnetwork' freq=2412 MHz)
wlan1: Associated with 02:00:00:00:00:00
wlan1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlan1: WPA: Key negotiation completed with 02:00:00:00:00:00 [PTK=CCMP GTK=CCMP]
wlan1: CTRL-EVENT-CONNECTED - Connection to 02:00:00:00:00:00 completed [id=0 id_str=]
[22:02:37] Loaded pairwise and group encryption keys.
[22:02:37] Trigger = Connected.
[22:02:37] Generating queue-saquery test case.
[22:02:38] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=02:00:00:00:00:00 (RA=DA) addr2=02:00:00:00:01:00 (TA=SA) addr3=02:00:00:00:00:00 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[22:02:40] Injected <Dot11  subtype=Association Request type=Management addr1=02:00:00:00:00:00 (RA=DA) addr2=02:00:00:00:01:00 (TA=SA) addr3=02:00:00:00:00:00 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[22:02:44] 802.11 Management Deauthentication 02:00:00:00:00:00 (TA=SA) > 02:00:00:00:01:00 (RA=DA) / Dot11Deauth
[22:02:44] Detected an unprotected deauthentication frame from AP.
[22:02:44] Trigger = Received.
[22:02:46] Disconnecting.
p2p-dev-wlan1: CTRL-EVENT-DSCP-POLICY clear_all
[22:02:46] Closing daemon and cleaning up ...
p2p-dev-wlan1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=p2p-dev-wlan1 disabled_11b_rates=0
p2p-dev-wlan1: CTRL-EVENT-TERMINATING 
wlan1: CTRL-EVENT-DISCONNECTED bssid=02:00:00:00:00:00 reason=3 locally_generated=1
wlan1: CTRL-EVENT-DSCP-POLICY clear_all
wlan1: PMKSA-CACHE-REMOVED 02:00:00:00:00:00 0
wlan1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlan1 disabled_11b_rates=0
wlan1: CTRL-EVENT-TERMINATING 



