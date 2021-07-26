#!/usr/bin/env bash

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

chown pi:pi /var/lock/ili9341
chown pi:pi /var/lock/msbrowser

chmod 666 /var/lock/ili9341
chmod 666 /var/lock/msbrowser
