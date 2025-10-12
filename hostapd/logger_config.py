# logger_config.py
from loguru import logger
import sys

# Basic logger config used by all scripts.
logger.remove()  # remove default
logger.add(sys.stderr, level="INFO",
           format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>")
# To log to a file uncomment:
# logger.add("hostapd_tool.log", rotation="10 MB", level="INFO")
