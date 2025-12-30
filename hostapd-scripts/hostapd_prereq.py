#!/usr/bin/env python3
# hostapd_prereq.py
from logger_config import logger  # if not already imported
import shlex
import subprocess
import sys
import os
import time
from logger_config import logger
import config

DNSMASQ_CONF = config.DNSMASQ_CONF_TEMPLATE.format(iface=config.IFACE)
DNSMASQ_PID_FILE = config.DNSMASQ_PID_FILE_TEMPLATE.format(iface=config.IFACE)


def run_cmd(cmd, sudo=True, capture=False):
    full_cmd = cmd if not sudo else ["sudo"] + cmd
    if capture:
        return subprocess.run(full_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return subprocess.run(full_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# NAT / iptables internet sharing helpers (optional)

def enable_internet_sharing(inet_iface=None, ap_iface=None):
    inet = inet_iface or config.INET_IFACE
    ap = ap_iface or config.IFACE
    logger.info(f"Enabling internet sharing: {inet} -> {ap}")

    # Turn on IP forwarding
    run_cmd(["sysctl", "-w", "net.ipv4.ip_forward=1"])

    # Add NAT and forward rules (best-effort)
    run_cmd(["iptables", "-t", "nat", "-A", "POSTROUTING",
            "-o", inet, "-j", "MASQUERADE"])
    run_cmd(["iptables", "-A", "FORWARD", "-i", inet, "-o", ap, "-m",
            "state", "--state", "RELATED,ESTABLISHED", "-j", "ACCEPT"])
    run_cmd(["iptables", "-A", "FORWARD", "-i", ap, "-o", inet, "-j", "ACCEPT"])

    logger.success("Internet sharing enabled (iptables rules added).")


def disable_internet_sharing():
    logger.info(
        "Disabling internet sharing and cleaning iptables rules (best-effort)")

    # Turn off forwarding (best-effort)
    run_cmd(["sysctl", "-w", "net.ipv4.ip_forward=0"])

    # Flush NAT + filter rules (best-effort; conservative flush for our use-case)
    run_cmd(["iptables", "-t", "nat", "-F"])
    run_cmd(["iptables", "-F"])
    run_cmd(["iptables", "-X"])

    logger.success("Internet sharing disabled (iptables rules flushed).")


def prepare():
    logger.info(f"Preparing interface {config.IFACE} for hostapd...")
    run_cmd(["nmcli", "device", "set", config.IFACE, "managed", "no"])
    run_cmd(["ip", "link", "set", config.IFACE, "up"])
    run_cmd(["ip", "addr", "flush", "dev", config.IFACE])
    run_cmd(["ip", "addr", "add", config.STATIC_IP, "dev", config.IFACE])

    logger.info(f"Creating dnsmasq config: {DNSMASQ_CONF}")
    with open(DNSMASQ_CONF, "w") as f:
        f.write(
            f"interface={config.IFACE}\n"
            f"dhcp-range={config.DHCP_RANGE_START},{config.DHCP_RANGE_END},{config.DHCP_LEASE}\n"
            f"bind-interfaces\n"
            f"pid-file={DNSMASQ_PID_FILE}\n"
        )

    # kill possible previous dnsmasq instances (best effort)
    run_cmd(["pkill", "dnsmasq"])

    logger.info("Starting dnsmasq (detached)...")
    with open(os.devnull, "w") as devnull:
        subprocess.Popen(
            ["sudo", "dnsmasq", "-C", DNSMASQ_CONF],
            stdout=devnull,
            stderr=devnull,
            preexec_fn=os.setpgrp
        )

    logger.success(f"Interface {config.IFACE} prepared. Run hostapd with:")
    logger.info(
        f"    sudo ./{config.HOSTAPD_DEST_DIR}/hostapd {config.HOSTAPD_CONF} [-dd]")
    time.sleep(config.SLEEP_BETWEEN_STEPS)


def restore():
    logger.info(f"Restoring interface {config.IFACE} to managed state...")
    run_cmd(["ip", "addr", "flush", "dev", config.IFACE])
    run_cmd(["ip", "link", "set", config.IFACE, "down"])
    run_cmd(["ip", "link", "set", config.IFACE, "up"])
    run_cmd(["nmcli", "device", "set", config.IFACE, "managed", "yes"])

    # best-effort kill of dnsmasq associated with interface
    run_cmd(["pkill", "-f", f"dnsmasq.*{config.IFACE}"])

    # cleanup files if exist
    for f in [DNSMASQ_CONF, DNSMASQ_PID_FILE]:
        try:
            os.remove(f)
            logger.debug(f"Removed temp file: {f}")
        except FileNotFoundError:
            logger.debug(f"Temp file not found (ok): {f}")
    # disable sharing if present
    try:
        disable_internet_sharing()
    except Exception:
        logger.debug(
            "disable_internet_sharing() raised an exception; continuing cleanup")

    logger.success(
        f"Interface {config.IFACE} restored. Wi-Fi should work normally.")
    time.sleep(config.SLEEP_BETWEEN_STEPS)


def usage_and_exit():
    print(f"Usage: {sys.argv[0]} <prepare|restore>")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["prepare", "restore", "enable-share", "disable-share"]:
        usage_and_exit()

    try:
        cmd = sys.argv[1]
        if cmd == "prepare":
            prepare()
        elif cmd == "restore":
            restore()
        elif cmd == "enable-share":
            enable_internet_sharing()
        elif cmd == "disable-share":
            disable_internet_sharing()
    except KeyboardInterrupt:
        logger.warning(
            "Interrupted by user — attempting to restore interface.")
        # on interrupt, attempt restore
        restore()
    finally:
        # make sure terminal state sane
        os.system("stty sane")
