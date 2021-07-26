#!/bin/bash
# raspi-hostname.sh
# By Weston Ruter (@westonruter)
# Adapted from https://github.com/asb/raspi-config/blob/351ba30f11403a4a7b80e76428018eff565b8cf1/raspi-config#L202-L218

# Set the hostname of the Pi to be 'raspberrypi-' followed by the processor serial without leading zeros
# If the hostname has already been set, then no action is taken. In both cases, the name is written to STDOUT.
# Any other messages are written to STDERR. If not run on a Pi (where /home/pi does not exist), then the script aborts.
# Example hostname: raspberrypi-a1b2c3

if [ ! -e /home/pi ]; then
    echo "Only run this on your pi."
    exit 1
fi

CURRENT_HOSTNAME=`cat /etc/hostname | tr -d " \t\n\r"`
#NEW_HOSTNAME=raspberrypi-$(cat /proc/cpuinfo | grep -E "^Serial" | sed "s/.*: 0*//")
if [ "$CURRENT_HOSTNAME" == "$NEW_HOSTNAME" ]; then
    echo "Current hostname already set to:" >&2
    echo $NEW_HOSTNAME
    exit 0
else
    exit 1    
fi

echo "Changing hostname from $CURRENT_HOSTNAME to $NEW_HOSTNAME..." >&2
echo $NEW_HOSTNAME | sudo tee /etc/hostname > /dev/null
sudo sed -i "s/127.0.1.1.*$CURRENT_HOSTNAME\$/127.0.1.1\t$NEW_HOSTNAME/g" /etc/hosts

echo "Hostname changed to:" >&2
echo $NEW_HOSTNAME
echo "Restart your pi for change to take effect." >&2
