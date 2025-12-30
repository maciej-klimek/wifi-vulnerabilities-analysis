(venv) ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Desktop/wifi/macstealer/research (main*) » sudo ./macstealer.py wlxa82948afa417 --ping --flip                                                        atis@atis-Latitude-5420
[22:27:52] Note: remember to disable Wi-Fi in your network manager so it doesn't interfere with this script
[22:27:52] Starting wpa_supplicant using: ../wpa_supplicant/wpa_supplicant -Dnl80211 -i wlxa82948afa417 -c client.conf -W
Successfully initialized wpa_supplicant
[22:27:53] Switching the victim and attacker identities.
[22:27:53] Scanning for network and connecting as victim user...
wlxa82948afa417: CTRL-EVENT-DSCP-POLICY clear_all
wlxa82948afa417: Trying to associate with c4:e9:84:af:7a:60 (SSID='testnetwork' freq=2412 MHz)
wlxa82948afa417: CTRL-EVENT-STARTED-CHANNEL-SWITCH freq=2412 ht_enabled=1 ch_offset=1 ch_width=40 MHz cf1=2422 cf2=0
wlxa82948afa417: Associated with c4:e9:84:af:7a:60
wlxa82948afa417: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlxa82948afa417: WPA: Key negotiation completed with c4:e9:84:af:7a:60 [PTK=CCMP GTK=CCMP]
wlxa82948afa417: CTRL-EVENT-CONNECTED - Connection to c4:e9:84:af:7a:60 completed [id=1 id_str=attacker]
[22:27:55] Sending DHCP discover with XID 736692297
[22:27:55] Received DHCP offer for 192.168.1.101, sending DHCP request.
[22:27:55] Sending DHCP request with XID 736692297
[22:27:55] DHCP ACK: Got IP address 192.168.1.101/a8:29:48:af:a4:17 with router at 192.168.1.1/c4:e9:84:af:7a:60.
[22:27:55] Transmitting challenge TCP SYN packet to 8.8.8.8:443
[22:27:55] Transmitted packet: <Ether  dst=c4:e9:84:af:7a:60 src=a8:29:48:af:a4:17 type=IPv4 |<IP  frag=0 proto=tcp src=192.168.1.101 dst=8.8.8.8 |<TCP  sport=11867 dport=https seq=481885790 |>>>
[22:27:55] Transmitted packet: <Ether  dst=c4:e9:84:af:7a:60 src=a8:29:48:af:a4:17 type=IPv4 |<IP  frag=0 proto=tcp src=192.168.1.101 dst=8.8.8.8 |<TCP  sport=11867 dport=https seq=481885790 |>>>
[22:27:55] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=11867 seq=1534432391 ack=481885791 dataofs=6 reserved=0 flags=SA window=65535 chksum=0x8afe urgptr=0 options=[('MSS', 1412)] |>>>
[22:27:55] Received SYN/ACK 0.02878093719482422 seconds after sending SYN.
[22:27:55] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=11867 seq=1534432391 ack=481885791 dataofs=6 reserved=0 flags=SA window=65535 chksum=0x8afe urgptr=0 options=[('MSS', 1412)] |>>>
[22:27:55] Received SYN/ACK 0.03046870231628418 seconds after sending SYN.
[22:27:58] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=11867 seq=1534432391 ack=481885791 dataofs=6 reserved=0 flags=SA window=65535 chksum=0x8afe urgptr=0 options=[('MSS', 1412)] |>>>
[22:27:58] Received SYN/ACK 2.3985774517059326 seconds after sending SYN.
[22:28:02] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=11867 seq=1534432391 ack=481885791 dataofs=6 reserved=0 flags=SA window=65535 chksum=0x8afe urgptr=0 options=[('MSS', 1412)] |>>>
[22:28:02] Received SYN/ACK 6.42481255531311 seconds after sending SYN.
WARNING: No route found for IPv4 destination 192.168.1.1 (no default route?)
[22:28:07] c4:e9:84:af:7a:60: ARP: Ether / ARP who has 192.168.1.101 says 192.168.1.1 ==> Ether / ARP is at a8:29:48:af:a4:17 says 192.168.1.101 on lo
[22:28:10] Received TCP response: <Ether  dst=a8:29:48:af:a4:17 src=c4:e9:84:af:7a:60 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=117 proto=tcp chksum=0x33af src=8.8.8.8 dst=192.168.1.101 |<TCP  sport=https dport=11867 seq=1534432391 ack=481885791 dataofs=6 reserved=0 flags=SA window=65535 chksum=0x8afe urgptr=0 options=[('MSS', 1412)] |>>>
[22:28:10] Received SYN/ACK 15.006066799163818 seconds after sending SYN.
[22:28:15] >>> Ping test done, everything looks good so far. You can continue with other tests.
[22:28:15] Closing daemon and cleaning up ...
wlxa82948afa417: CTRL-EVENT-DISCONNECTED bssid=c4:e9:84:af:7a:60 reason=3 locally_generated=1
wlxa82948afa417: CTRL-EVENT-DSCP-POLICY clear_all
wlxa82948afa417: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlxa82948afa417 disabled_11b_rates=0
wlxa82948afa417: CTRL-EVENT-TERMINATING 