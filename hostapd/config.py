# config.py
# Central configuration used by all hostapd helper scripts.

# Packages required for building hostapd
BUILD_DEPENDENCIES = [
    "build-essential",
    "libssl-dev",
    "libnl-3-dev",
    "libnl-genl-3-dev",
    "pkg-config",
    "libsqlite3-dev",
    "libpcre3-dev",
]
INSTALL_BUILD_DEPS = True  # if False, skip auto-install


# Network / interface
IFACE = "wlo1"
STATIC_IP = "192.168.12.1/24"
DHCP_RANGE_START = "192.168.12.2"
DHCP_RANGE_END = "192.168.12.50"
DHCP_LEASE = "12h"

# Internet sharing (optional)
INET_IFACE = "enp3s0"       # interface that has internet access (Ethernet)
ENABLE_INTERNET_BY_DEFAULT = False  # keep sharing off by default


# Hostapd sources / build
HOSTAPD_VERSION = "2.11"
HOSTAPD_TAR = f"hostapd-{HOSTAPD_VERSION}.tar.gz"
HOSTAPD_SRC_DIR = f"hostapd-{HOSTAPD_VERSION}"
# subdir inside the extracted archive where Makefile lives
HOSTAPD_BUILD_SUBDIR = "hostapd"
# where compiled binary will be copied (hostapd/hostapd)
HOSTAPD_DEST_DIR = "hostapd"

# Paths for configs and runtime files
# local .config that will be copied into sources before build
LOCAL_CONFIG_FILE = ".config"
HOSTAPD_CONF = "hostapd.conf"      # runtime hostapd.conf used to run hostapd
DNSMASQ_CONF_TEMPLATE = "/tmp/dnsmasq_{iface}.conf"
DNSMASQ_PID_FILE_TEMPLATE = "/tmp/dnsmasq_{iface}.pid"

# Build settings
MAKE_JOBS = 4

# Terminal / runtime
GNOME_TERMINAL_CMD = "gnome-terminal"  # assume gnome-terminal available
DEFAULT_SHELL = "zsh"                  # open new terminal with zsh

# Timing / UX
PAUSE_MSG = "Press ENTER to continue..."
# seconds (scripts will also use press-enter; this is a small extra wait)
SLEEP_BETWEEN_STEPS = 1.0

# Other
REMOVE_ITEMS = [
    HOSTAPD_DEST_DIR,
    HOSTAPD_SRC_DIR,
    HOSTAPD_TAR
]
