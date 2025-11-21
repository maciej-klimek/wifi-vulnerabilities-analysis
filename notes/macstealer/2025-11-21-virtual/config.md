 ifconfig
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 68774  bytes 6570796 (6.5 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 68774  bytes 6570796 (6.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.100.1  netmask 255.255.255.0  broadcast 192.168.100.255
        ether 02:00:00:00:00:00  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 16  bytes 2616 (2.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 02:00:00:00:01:00  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan2: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 192.168.100.10  netmask 255.255.255.0  broadcast 192.168.100.255
        ether 02:00:00:00:02:00  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 16 overruns 0  carrier 0  collisions 0

wlo1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.16  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::7fb7:ee29:8666:52a3  prefixlen 64  scopeid 0x20<link>
        ether a0:51:0b:65:8e:70  txqueuelen 1000  (Ethernet)
        RX packets 30569  bytes 25835875 (25.8 MB)
        RX errors 0  dropped 236  overruns 0  frame 0
        TX packets 14655  bytes 7038793 (7.0 MB)
        TX errors 0  dropped 11 overruns 0  carrier 0  collisions 0

❯ iw dev
phy#13
        Interface wlan2
                ifindex 19
                wdev 0xd00000001
                addr 02:00:00:00:02:00
                type managed
                txpower 20.00 dBm
                multicast TXQ:
                        qsz-byt qsz-pkt flows   drops   marks   overlmt hashcol tx-bytes        tx-packets
                        0       0       0       0       0       0       0       0               0
phy#12
        Unnamed/non-netdev interface
                wdev 0xc00000002
                addr 42:00:00:00:01:00
                type P2P-device
                txpower 20.00 dBm
        Interface wlan1
                ifindex 18
                wdev 0xc00000001
                addr 02:00:00:00:01:00
                type managed
                txpower 20.00 dBm
                multicast TXQ:
                        qsz-byt qsz-pkt flows   drops   marks   overlmt hashcol tx-bytes        tx-packets
                        0       0       0       0       0       0       0       0               0
phy#11
        Unnamed/non-netdev interface
                wdev 0xb00000002
                addr 42:00:00:00:00:00
                type P2P-device
                txpower 20.00 dBm
        Interface wlan0
                ifindex 17
                wdev 0xb00000001
                addr 02:00:00:00:00:00
                ssid testnetwork
                type AP
                channel 1 (2412 MHz), width: 20 MHz, center1: 2412 MHz
                txpower 20.00 dBm
                multicast TXQ:
                        qsz-byt qsz-pkt flows   drops   marks   overlmt hashcol tx-bytes        tx-packets
                        0       0       5       0       0       0       0       1592            5
phy#7
        Interface wlo1
                ifindex 12
                wdev 0x700000001
                addr a0:51:0b:65:8e:70
                ssid PowinnoSmigac
                type managed
                channel 13 (2472 MHz), width: 20 MHz, center1: 2472 MHz
                txpower 20.00 dBm
                multicast TXQ:
                        qsz-byt qsz-pkt flows   drops   marks   overlmt hashcol tx-bytes        tx-packets
                        0       0       0       0       0       0       0       0               0