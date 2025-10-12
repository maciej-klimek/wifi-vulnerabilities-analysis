#!/usr/bin/env python3
# hostapd_build.py
import os
import shutil
import subprocess
import time

from logger_config import logger
import config


def build_hostapd():
    hostapd_dir = os.path.join(
        config.HOSTAPD_SRC_DIR, config.HOSTAPD_BUILD_SUBDIR)
    config_src = config.LOCAL_CONFIG_FILE
    config_dst = os.path.join(hostapd_dir, ".config")

    if not os.path.exists(hostapd_dir):
        logger.error(
            f"Hostapd build directory not found: {hostapd_dir}. Run download first.")
        raise FileNotFoundError(hostapd_dir)

    if not os.path.exists(config_src):
        logger.error(f"Local .config file missing: {config_src}")
        raise FileNotFoundError(config_src)

    logger.info(f"Copying {config_src} to {config_dst} ...")
    shutil.copy(config_src, config_dst)

    logger.info("Starting build (make)...")
    make_cmd = ["make", "-C", hostapd_dir, f"-j{config.MAKE_JOBS}"]
    try:
        subprocess.run(make_cmd, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Build failed: {e}")
        raise

    # ensure destination dir exists
    os.makedirs(config.HOSTAPD_DEST_DIR, exist_ok=True)
    src_bin = os.path.join(hostapd_dir, "hostapd")
    dst_bin = os.path.join(config.HOSTAPD_DEST_DIR, "hostapd")
    if not os.path.exists(src_bin):
        logger.error(f"Built binary not found: {src_bin}")
        raise FileNotFoundError(src_bin)

    logger.info(f"Copying binary to {dst_bin} ...")
    shutil.copy(src_bin, dst_bin)
    logger.success(f"Build finished and binary available at {dst_bin}")
    time.sleep(config.SLEEP_BETWEEN_STEPS)


if __name__ == "__main__":
    build_hostapd()
