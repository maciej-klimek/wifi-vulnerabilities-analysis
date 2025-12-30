~/Desktop/wifi/macstealer/research (main*) » sudo ./macstealer.py wlxa82948afa417 --ping                                                               atis@atis-Latitude-5420
[22:22:59] Note: remember to disable Wi-Fi in your network manager so it doesn't interfere with this script
[22:22:59] Starting wpa_supplicant using: ../wpa_supplicant/wpa_supplicant -Dnl80211 -i wlxa82948afa417 -c client.conf -W
Successfully initialized wpa_supplicant
[22:22:59] Scanning for network and connecting as victim user...
wlxa82948afa417: CTRL-EVENT-DSCP-POLICY clear_all
wlxa82948afa417: Trying to associate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlxa82948afa417: CTRL-EVENT-STARTED-CHANNEL-SWITCH freq=2412 ht_enabled=1 ch_offset=1 ch_width=40 MHz cf1=2422 cf2=0
wlxa82948afa417: Associated with c4:e9:84:af:7a:60
wlxa82948afa417: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlxa82948afa417: WPA: Key negotiation completed with c4:e9:84:af:7a:60 [PTK=CCMP GTK=CCMP]
wlxa82948afa417: CTRL-EVENT-CONNECTED - Connection to c4:e9:84:af:7a:60 completed [id=0 id_str=victim]
[22:23:01] Sending DHCP discover with XID 322792633
[22:23:01] Received DHCP offer for 192.168.1.101, sending DHCP request.
[22:23:01] Sending DHCP request with XID 322792633
[22:23:01] DHCP ACK: Got IP address 192.168.1.101/a8:29:48:af:a4:17 with router at 192.168.1.1/c4:e9:84:af:7a:60.
[22:23:01] Transmitting challenge TCP SYN packet to 8.8.8.8:443
[22:23:01] Transmitted packet: <Ether  dst=c4:e9:84:af:7a:60 src=a8:29:48:af:a4:17 type=IPv4 |<IP  frag=0 proto=tcp src=192.168.1.101 dst=8.8.8.8 |<TCP  sport=22869 dport=https seq=1274629827 |>>>
[22:23:01] Transmitted packet: <Ether  dst=c4:e9:84:af:7a:60 src=a8:29:48:af:a4:17 type=IPv4 |<IP  frag=0 proto=tcp src=192.168.1.101 dst=8.8.8.8 |<TCP  sport=22869 dport=https seq=1274629827 |>>>
[22:23:01] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=22869 seq=1015787248 ack=1274629828 dataofs=6 reserved=0 flags=SA window=65535 chksum=0xe4df urgptr=0 options=[('MSS', 1412)] |>>>
[22:23:01] Received SYN/ACK 0.028900623321533203 seconds after sending SYN.
[22:23:01] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=22869 seq=1015787248 ack=1274629828 dataofs=6 reserved=0 flags=SA window=65535 chksum=0xe4df urgptr=0 options=[('MSS', 1412)] |>>>
[22:23:01] Received SYN/ACK 0.030086755752563477 seconds after sending SYN.
[22:23:02] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=22869 seq=1015787248 ack=1274629828 dataofs=6 reserved=0 flags=SA window=65535 chksum=0xe4df urgptr=0 options=[('MSS', 1412)] |>>>
[22:23:02] Received SYN/ACK 0.3341560363769531 seconds after sending SYN.
[22:23:04] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=22869 seq=1015787248 ack=1274629828 dataofs=6 reserved=0 flags=SA window=65535 chksum=0xe4df urgptr=0 options=[('MSS', 1412)] |>>>
[22:23:04] Received SYN/ACK 2.342019557952881 seconds after sending SYN.
WARNING: No route found for IPv4 destination 192.168.1.1 (no default route?)
[22:23:06] c4:e9:84:af:7a:60: ARP: Ether / ARP who has 192.168.1.101 says 192.168.1.1 ==> Ether / ARP is at a8:29:48:af:a4:17 says 192.168.1.101 on lo
[22:23:08] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=22869 seq=1015787248 ack=1274629828 dataofs=6 reserved=0 flags=SA window=65535 chksum=0xe4df urgptr=0 options=[('MSS', 1412)] |>>>
[22:23:08] Received SYN/ACK 6.372397184371948 seconds after sending SYN.
[22:23:21] >>> Ping test done. Consider using a server that retransmits SYN/ACK for a longer time.
[22:23:21] Closing daemon and cleaning up ...
wlxa82948afa417: CTRL-EVENT-DISCONNECTED bssid=c4:e9:84:af:7a:60 reason=3 locally_generated=1
wlxa82948afa417: CTRL-EVENT-DSCP-POLICY clear_all
wlxa82948afa417: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlxa82948afa417 disabled_11b_rates=0
wlxa82948afa417: CTRL-EVENT-TERMINATING 