#!/usr/bin/env python3
import os
import subprocess
import tarfile
import urllib.request

HOSTAPD_VERSION = "2.11"
SRC_URL = f"https://w1.fi/releases/hostapd-{HOSTAPD_VERSION}.tar.gz"
SRC_ARCHIVE = f"hostapd-{HOSTAPD_VERSION}.tar.gz"
SRC_DIR = f"hostapd-{HOSTAPD_VERSION}"


def download_hostapd():
    if os.path.exists(SRC_DIR):
        print(f"[*] Źródła hostapd już istnieją: {SRC_DIR}")
        return
    print("[*] Pobieranie źródeł hostapd...")
    urllib.request.urlretrieve(SRC_URL, SRC_ARCHIVE)
    print("[*] Rozpakowywanie źródeł...")
    with tarfile.open(SRC_ARCHIVE, "r:gz") as tar:
        tar.extractall()
    print(f"[*] Źródła rozpakowane do {SRC_DIR}")


if __name__ == "__main__":
    download_hostapd()
