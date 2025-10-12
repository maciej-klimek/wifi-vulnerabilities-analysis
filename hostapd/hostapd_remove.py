#!/usr/bin/env python3
# hostapd_remove.py
import os
import shutil
import time
from logger_config import logger
import config


def safe_remove(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
            logger.info(f"Removed directory: {path}")
        else:
            os.remove(path)
            logger.info(f"Removed file: {path}")
    else:
        logger.debug(f"Not present, skipping: {path}")


def main():
    logger.info("Removing hostapd build resources...")
    for item in config.REMOVE_ITEMS:
        safe_remove(item)
    logger.success("Cleanup completed successfully.")
    time.sleep(config.SLEEP_BETWEEN_STEPS)


if __name__ == "__main__":
    main()
