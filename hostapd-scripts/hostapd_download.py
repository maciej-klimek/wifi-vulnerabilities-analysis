#!/usr/bin/env python3
# hostapd_download.py
import os
import tarfile
import urllib.request
import time

from logger_config import logger
import config


def download_hostapd():
    tar_name = config.HOSTAPD_TAR
    src_dir = config.HOSTAPD_SRC_DIR

    if os.path.exists(src_dir):
        logger.info(
            f"Hostapd sources already exist: {src_dir} — skipping download.")
        return

    url = f"https://w1.fi/releases/{tar_name}"
    logger.info(f"Downloading hostapd {config.HOSTAPD_VERSION} from {url} ...")
    try:
        urllib.request.urlretrieve(url, tar_name)
    except Exception as e:
        logger.error(f"Failed to download {url}: {e}")
        raise

    logger.info(f"Extracting {tar_name} ...")
    try:
        with tarfile.open(tar_name, "r:gz") as tar:
            tar.extractall()
    except Exception as e:
        logger.error(f"Failed to extract {tar_name}: {e}")
        raise

    logger.success(f"Sources extracted to {src_dir}")
    time.sleep(config.SLEEP_BETWEEN_STEPS)


if __name__ == "__main__":
    download_hostapd()
