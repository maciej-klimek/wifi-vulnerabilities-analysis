#!/usr/bin/env python3
import os
import shutil


def safe_remove(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"[*] Removed directory: {path}")
        else:
            os.remove(path)
            print(f"[*] Removed file: {path}")


def main():
    print("[*] Removing hostapd build resources...")
    safe_remove("hostapd")
    safe_remove("hostapd-2.11")
    safe_remove("hostapd-2.11.tar.gz")
    print("[+] Cleanup completed successfully.")


if __name__ == "__main__":
    main()
