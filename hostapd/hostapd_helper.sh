#!/bin/bash

# Usage:
# ./hostapd_dhcp_helper.sh prepare wlo1
# ./hostapd_dhcp_helper.sh restore wlo1

ACTION=$1
IFACE=$2

if [[ -z "$ACTION" || -z "$IFACE" ]]; then
    echo "Usage: $0 <prepare|restore> <interface>"
    exit 1
fi

HOSTAPD_CONF="./hostapd.conf"
STATIC_IP="192.168.12.1/24"
DHCP_RANGE_START="192.168.12.2"
DHCP_RANGE_END="192.168.12.50"
DNSMASQ_CONF="/tmp/dnsmasq_${IFACE}.conf"

prepare() {
    echo "[*] Preparing interface $IFACE for hostapd + DHCP..."

    sudo nmcli device set "$IFACE" managed no
    sudo ip link set "$IFACE" up
    sudo ip addr flush dev "$IFACE"
    sudo ip addr add $STATIC_IP dev "$IFACE"

    DNSMASQ_CONF="/tmp/dnsmasq_$IFACE.conf"
    sudo pkill dnsmasq
    sudo tee $DNSMASQ_CONF > /dev/null <<EOF
interface=$IFACE
dhcp-range=192.168.12.2,192.168.12.50,12h
bind-interfaces
EOF

    sudo dnsmasq -C $DNSMASQ_CONF

    echo "[*] Interface prepared. You can now start hostapd:"
    echo "sudo ./hostapd/hostapd $HOSTAPD_CONF -dd"
}

restore() {
    echo "[*] Restoring interface $IFACE..."

    sudo pkill -f "dnsmasq.*$DNSMASQ_CONF"
    sudo rm -f $DNSMASQ_CONF

    sudo ip addr flush dev "$IFACE"
    sudo ip link set "$IFACE" down
    sudo ip link set "$IFACE" up

    sudo nmcli device set "$IFACE" managed yes

    echo "[*] Interface restored. Wi-Fi should work as normal."
}

case $ACTION in
    prepare)
        prepare
        ;;
    restore)
        restore
        ;;
    *)
        echo "Invalid action: $ACTION. Use prepare or restore."
        exit 1
        ;;
esac
