#!/bin/bash
#mac=`cat /sys/class/net/eth0/address`
#mac1="${mac:$i:5}"

# lookup the location name based on mac address
l=$(cat locations.txt | grep `cat /sys/class/net/eth0/address` | awk '{print $2}')
hostname="rpi-t-${l}"

raspi-config nonint do_hostname "$hostname"
hostname -b "$hostname"
systemctl restart avahi-daemon
