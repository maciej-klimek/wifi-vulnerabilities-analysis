root@atis-Latitude-5420:/home/atis/Desktop/wifi/macstealer/research# python3 macstealer.py wlp0s20f3
[20:56:48] Note: remember to disable Wi-Fi in your network manager so it doesn't interfere with this script
[20:56:48] Starting wpa_supplicant using: ../wpa_supplicant/wpa_supplicant -Dnl80211 -i wlp0s20f3 -c client.conf -W
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
[20:56:48] Note: Victim and attacker are using the same password PSK{12345678}. In this scenario
[20:56:48]       the attack may be less damaging, see the Threat Model Discussion in README.md.
[20:56:48] Scanning for network and connecting as victim user...
wlp0s20f3: CTRL-EVENT-DSCP-POLICY clear_all
wlp0s20f3: SME: Trying to authenticate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlp0s20f3: Trying to associate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlp0s20f3: Associated with c4:e9:84:af:7a:60
wlp0s20f3: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlp0s20f3: WPA: Key negotiation completed with c4:e9:84:af:7a:60 [PTK=CCMP GTK=CCMP]
wlp0s20f3: CTRL-EVENT-CONNECTED - Connection to c4:e9:84:af:7a:60 completed [id=0 id_str=victim]
[20:56:50] Sending DHCP discover with XID 1779512154
[20:56:50] Received DHCP offer for 192.168.1.102, sending DHCP request.
[20:56:50] Sending DHCP request with XID 1779512154
[20:56:50] DHCP ACK: Got IP address 192.168.1.102/ec:63:d7:89:d5:5a with router at 192.168.1.1/c4:e9:84:af:7a:60.
[20:56:50] Transmitting challenge TCP SYN packet to 8.8.8.8:443
[20:56:50] Transmitted packet: <Ether  dst=c4:e9:84:af:7a:60 src=ec:63:d7:89:d5:5a type=IPv4 |<IP  frag=0 proto=tcp src=192.168.1.102 dst=8.8.8.8 |<TCP  sport=10370 dport=https seq=663010456 |>>>
[20:56:50] Transmitted packet: <Ether  dst=c4:e9:84:af:7a:60 src=ec:63:d7:89:d5:5a type=IPv4 |<IP  frag=0 proto=tcp src=192.168.1.102 dst=8.8.8.8 |<TCP  sport=10370 dport=https seq=663010456 |>>>
[20:56:50] Received TCP response: <Ether  dst=ec:63:d7:89:d5:5a src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33ae src=8.8.8.8 dst=192.168.1.102 |<TCP  sport=https dport=10370 seq=3341073111 ack=663010457 dataofs=6 reserved=0 flags=SA window=65535 chksum=0x35d1 urgptr=0 options=[('MSS', 1412)] |>>>
[20:56:50] Received TCP response: <Ether  dst=ec:63:d7:89:d5:5a src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33ae src=8.8.8.8 dst=192.168.1.102 |<TCP  sport=https dport=10370 seq=3341073111 ack=663010457 dataofs=6 reserved=0 flags=SA window=65535 chksum=0x35d1 urgptr=0 options=[('MSS', 1412)] |<Padding  load=b'  ' |>>>>
[20:56:50] Reconnecting as the attacker...
wlp0s20f3: CTRL-EVENT-DISCONNECTED bssid=c4:e9:84:af:7a:60 reason=3 locally_generated=1
wlp0s20f3: CTRL-EVENT-DSCP-POLICY clear_all
wlp0s20f3: CTRL-EVENT-REGDOM-CHANGE init=CORE type=WORLD
wlp0s20f3: SME: Trying to authenticate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlp0s20f3: Trying to associate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlp0s20f3: Associated with c4:e9:84:af:7a:60
wlp0s20f3: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlp0s20f3: WPA: Key negotiation completed with c4:e9:84:af:7a:60 [PTK=CCMP GTK=CCMP]
wlp0s20f3: CTRL-EVENT-CONNECTED - Connection to c4:e9:84:af:7a:60 completed [id=1 id_str=attacker]
[20:56:53] Listening for replies to the victim's TCP SYN request...
[20:56:53] Sending DHCP request with XID 1779512154
[20:56:53] Received TCP response: <Ether  dst=ec:63:d7:89:d5:5a src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33ae src=8.8.8.8 dst=192.168.1.102 |<TCP  sport=https dport=10370 seq=3341073111 ack=663010457 dataofs=6 reserved=0 flags=SA window=65535 chksum=0x35d1 urgptr=0 options=[('MSS', 1412)] |<Padding  load=b'  ' |>>>>
[20:56:53] >>> Attacker PSK{12345678} intercepted TCP SYN/ACK reply to victim PSK{12345678} after 2.4s.
[20:56:53] >>> This means the network is vulnerable!
[20:56:53] Closing daemon and cleaning up ...
p2p-dev-wlp0s20: CTRL-EVENT-DSCP-POLICY clear_all
p2p-dev-wlp0s20: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=p2p-dev-wlp0s20 disabled_11b_rates=0
p2p-dev-wlp0s20: CTRL-EVENT-TERMINATING 
wlp0s20f3: CTRL-EVENT-DISCONNECTED bssid=c4:e9:84:af:7a:60 reason=3 locally_generated=1
wlp0s20f3: CTRL-EVENT-DSCP-POLICY clear_all
wlp0s20f3: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlp0s20f3 disabled_11b_rates=0
wlp0s20f3: CTRL-EVENT-TERMINATING 
root@atis-Latitude-5420:/home/atis/Desktop/wifi/macstealer/research# 


iw dev

root@atis-Latitude-5420:/home/atis/Desktop/wifi/macstealer/research# iw dev
phy#1
        Interface wlxa82948afa417
                ifindex 3
                wdev 0x100000001
                addr a8:29:48:af:a4:17
                type monitor
                txpower 12.00 dBm
phy#0
        Interface wlp0s20f3
                ifindex 2
                wdev 0x1
                addr ec:63:d7:89:d5:5a
                type managed
                txpower 22.00 dBm
                multicast TXQ:
                        qsz-byt qsz-pkt flows   drops   marks   overlmt hashcol tx-bytes        tx-packets
                        0       0       0       0       0       0       0       0               0
root@atis-Latitude-5420:/home/atis/Desktop/wifi/macstealer/research# 



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

