#!/usr/bin/env bash
# run_clean_test.sh
# Ensures a fresh environment (kills framework wpa_supplicant, removes leftover sockets,
# tries a global pmksa_flush), then starts the test.
# Usage: ./run_clean_test.sh <iface> <testname>
# Example: ./run_clean_test.sh wlo1 queue-4way-sleep

set -euo pipefail
IFACE=${1:-wlo1}
TEST=${2:-queue-4way-sleep}

echo "[*] Cleaning up any existing wpa_supplicant instances for ${IFACE}..."
# kill framework instances that reference the interface name
sudo pkill -f "wpa_supplicant.*${IFACE}" 2>/dev/null || true
sleep 0.15

echo "[*] Removing likely leftover control sockets (best-effort)..."
# best-effort removal of sockets named after the iface (careful)
sudo find / -type s -name "${IFACE}" -exec rm -f {} \; 2>/dev/null || true
sleep 0.05

echo "[*] Attempting global pmksa_flush (if global wpa_supplicant is running)..."
# best-effort flush on the default ctrl dir
if command -v wpa_cli >/dev/null 2>&1; then
  sudo wpa_cli -p /var/run/wpa_supplicant -i "${IFACE}" pmksa_flush || true
else
  echo "[!] wpa_cli not found in PATH; skipping global pmksa_flush"
fi
sleep 0.05

echo "[*] Start the AP/hotspot (if needed) now and confirm new SSID/PSK applied on phone."
echo "[*] Starting framework test: ./run.py ${IFACE} ${TEST}"
./run.py "${IFACE}" "${TEST}"
