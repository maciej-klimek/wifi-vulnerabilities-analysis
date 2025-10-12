
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

INTERFACE="wlo1"
IP_ADDRESS="192.168.100.1/24"

echo "Disabling Wi-Fi management by NetworkManager"
nmcli radio wifi off

echo "Unblocking Wi-Fi using rfkill"
rfkill unblock wifi

echo "Taking down interface $INTERFACE"
ip link set "$INTERFACE" down

echo "Setting interface $INTERFACE to AP mode"
iw "$INTERFACE" set type __ap

echo "Bringing up interface $INTERFACE"
ip link set "$INTERFACE" up

echo "Assigning IP address $IP_ADDRESS to $INTERFACE"
ip addr add "$IP_ADDRESS" dev "$INTERFACE"

echo "Wireless configuration:"
iwconfig
