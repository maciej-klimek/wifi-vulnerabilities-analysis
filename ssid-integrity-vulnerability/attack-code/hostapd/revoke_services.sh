#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

ACTION="$1"

if [[ "$ACTION" == "disable" ]]; then
  echo "Stopping, disabling, and masking systemd-resolved"
  systemctl stop systemd-resolved
  systemctl disable systemd-resolved
  systemctl mask systemd-resolved
  echo "systemd-resolved has been disabled and masked"
elif [[ "$ACTION" == "enable" ]]; then
  echo "Unmasking, enabling, and starting systemd-resolved"
  systemctl unmask systemd-resolved
  systemctl enable systemd-resolved
  systemctl start systemd-resolved
  echo "systemd-resolved has been restored"
else
  echo "Usage: $0 [disable|enable]"
  exit 1
fi
