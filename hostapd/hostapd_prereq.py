#!/usr/bin/env python3
import subprocess
import sys
import os
import signal

IFACE = "wlo1"
STATIC_IP = "192.168.12.1/24"
DNSMASQ_CONF = f"/tmp/dnsmasq_{IFACE}.conf"
DNSMASQ_PID_FILE = f"/tmp/dnsmasq_{IFACE}.pid"


def run_cmd(cmd):
    subprocess.run(cmd, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, check=False)


def prepare():
    print(f"[*] Preparing interface {IFACE}...")
    run_cmd(["sudo", "nmcli", "device", "set", IFACE, "managed", "no"])
    run_cmd(["sudo", "ip", "link", "set", IFACE, "up"])
    run_cmd(["sudo", "ip", "addr", "flush", "dev", IFACE])
    run_cmd(["sudo", "ip", "addr", "add", STATIC_IP, "dev", IFACE])

    with open(DNSMASQ_CONF, "w") as f:
        f.write(
            f"interface={IFACE}\n"
            f"dhcp-range=192.168.12.2,192.168.12.50,12h\n"
            f"bind-interfaces\n"
            f"pid-file={DNSMASQ_PID_FILE}\n"
        )

    run_cmd(["sudo", "pkill", "dnsmasq"])

    print("[*] Starting dnsmasq (detached)...")
    # Fully detached process (won’t screw terminal)
    with open(os.devnull, "w") as devnull:
        subprocess.Popen(
            ["sudo", "dnsmasq", "-C", DNSMASQ_CONF],
            stdout=devnull,
            stderr=devnull,
            preexec_fn=os.setpgrp  # detaches from controlling terminal
        )

    print(f"[*] Interface {IFACE} prepared. Run hostapd with:")
    print("    sudo ./hostapd/hostapd hostapd.conf -dd")


def restore():
    print(f"[*] Restoring interface {IFACE}...")

    subprocess.run(["sudo", "ip", "addr", "flush", "dev", IFACE])
    subprocess.run(["sudo", "ip", "link", "set", IFACE, "down"])
    subprocess.run(["sudo", "ip", "link", "set", IFACE, "up"])
    subprocess.run(["sudo", "nmcli", "device", "set", IFACE, "managed", "yes"])

    # Kill any dnsmasq process on this interface
    subprocess.run(
        ["sudo", "pkill", "-f", f"dnsmasq.*{IFACE}"], stderr=subprocess.DEVNULL)

    # Clean up temp files
    for f in [DNSMASQ_CONF, f"/tmp/dnsmasq_{IFACE}.pid"]:
        try:
            os.remove(f)
        except FileNotFoundError:
            pass

    print(f"[*] Interface {IFACE} restored. Wi-Fi should work normally.")



if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["prepare", "restore"]:
        print(f"Usage: {sys.argv[0]} <prepare|restore>")
        sys.exit(1)

    try:
        if sys.argv[1] == "prepare":
            prepare()
        else:
            restore()
    except KeyboardInterrupt:
        print("\n[!] Interrupted, restoring interface...")
        restore()
    finally:
        # ensures terminal stays clean even if something fails
        os.system("stty sane")
