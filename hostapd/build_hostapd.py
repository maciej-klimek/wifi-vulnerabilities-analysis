#!/usr/bin/env python3
import os
import subprocess
import shutil
import tarfile
import urllib.request

HOSTAPD_URL = "https://w1.fi/releases/hostapd-2.11.tar.gz"
SRC_DIR = "hostapd-2.11"
CONFIG_SRC = ".config"


def download_hostapd():
    if not os.path.exists(SRC_DIR):
        print("[*] Downloading hostapd-2.11...")
        tar_name = "hostapd-2.11.tar.gz"
        urllib.request.urlretrieve(HOSTAPD_URL, tar_name)
        print("[*] Extracting sources...")
        with tarfile.open(tar_name, "r:gz") as tar:
            tar.extractall(".")
        os.remove(tar_name)
    else:
        print("[*] Source already exists, skipping download.")


def build_hostapd():
    hostapd_dir = os.path.join(SRC_DIR, "hostapd")
    config_dest = os.path.join(hostapd_dir, ".config")

    print("[*] Copying custom .config to hostapd build directory...")
    shutil.copy(CONFIG_SRC, config_dest)

    print("[*] Building hostapd...")
    subprocess.run(["make", "-C", hostapd_dir, "-j4"], check=True)

    print("[*] Copying binary to ./hostapd/hostapd ...")
    os.makedirs("hostapd", exist_ok=True)
    shutil.copy(os.path.join(hostapd_dir, "hostapd"), "hostapd/hostapd")

    print("[+] Build completed successfully!")


if __name__ == "__main__":
    download_hostapd()
    build_hostapd()
