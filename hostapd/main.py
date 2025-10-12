#!/usr/bin/env python3
# main.py
import subprocess
import time
import os
import sys
from loguru import logger as _logger
from logger_config import logger
import config

PY = sys.executable  # path to python interpreter


def pause_prompt(msg=None):
    if msg is None:
        msg = config.PAUSE_MSG
    try:
        input(msg)
    except KeyboardInterrupt:
        logger.warning("Interrupted by user during pause.")


def run_script(script, args=None):
    args = args or []
    cmd = [PY, script] + args
    logger.info(f"Running: {' '.join(cmd)}")
    res = subprocess.run(cmd)
    if res.returncode != 0:
        logger.error(f"Script {script} exited with code {res.returncode}")
        raise SystemExit(res.returncode)
    logger.success(f"Script {script} finished successfully.")
    time.sleep(config.SLEEP_BETWEEN_STEPS)


def open_hostapd_in_terminal(debug=False):
    hostapd_bin = os.path.join(config.HOSTAPD_DEST_DIR, "hostapd")
    if not os.path.exists(hostapd_bin):
        logger.error(
            f"hostapd binary not found at {hostapd_bin}. Build first.")
        raise SystemExit(1)
    dd_flag = "-dd" if debug else ""
    cmd_line = f"sudo ./{config.HOSTAPD_DEST_DIR}/hostapd {config.HOSTAPD_CONF} {dd_flag}"
    # Keep terminal open after command so you can see output
    shell = config.DEFAULT_SHELL
    # gnome-terminal invocation
    term_cmd = [
        config.GNOME_TERMINAL_CMD,
        "--",
        shell,
        "-c",
        f"{cmd_line}; echo 'hostapd exited with $?: press ENTER to close this terminal'; read"
    ]
    logger.info(f"Opening new GNOME terminal to run hostapd: {cmd_line}")
    subprocess.Popen(term_cmd)
    time.sleep(1.0)


def menu_loop():
    logger.info("Entering interactive menu. Choose an action:")
    while True:
        print()
        print("  1) Stop hostapd (pkill)")
        print("  2) Restore interface (hostapd_prereq.py restore)")
        print("  3) Remove all components (hostapd_remove.py)")
        print("  q) Quit")
        choice = input("Select: ").strip().lower()
        if choice == "1":
            logger.info("Stopping hostapd with pkill...")
            subprocess.run(["sudo", "pkill", "hostapd"])
            logger.success("hostapd stop signal sent (pkill).")
        elif choice == "2":
            logger.info("Restoring interface...")
            run_script("hostapd_prereq.py", ["restore"])
        elif choice == "3":
            logger.info("Removing all components...")
            run_script("hostapd_remove.py")
        elif choice == "q":
            logger.info("Quitting interactive menu.")
            break
        else:
            logger.warning("Unknown selection, try again.")


def main():
    logger.info("Orchestrator started.")
    # 1) download
    run_script("hostapd_download.py")
    pause_prompt("Downloaded. Press ENTER to continue to build...")

    # 2) build
    run_script("hostapd_build.py")
    pause_prompt("Built. Press ENTER to continue to prepare interface...")

    # 3) prepare interface
    run_script("hostapd_prereq.py", ["prepare"])
    pause_prompt(
        "Interface prepared. Press ENTER to launch hostapd in new terminal...")

    # 4) ask debug option
    dd_resp = input("Run hostapd with debug (-dd)? [y/N]: ").strip().lower()
    debug_flag = dd_resp in ("y", "yes")

    # 5) open hostapd in new terminal
    open_hostapd_in_terminal(debug=debug_flag)
    logger.info("Hostapd started in new terminal.")

    # 6) interactive menu
    menu_loop()

    logger.info(
        "Main finished. You may still need to restore interface or remove components if desired.")
    # final hint
    logger.info("If you haven't already, run: python3 hostapd_prereq.py restore")
    logger.info("Or: python3 hostapd_remove.py")
    logger.success("Done.")


if __name__ == "__main__":
    main()
