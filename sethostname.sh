#!/bin/bash

mac=`cat /sys/class/net/eth0/address`
mac1="${mac:$i:5}"
hostname="raspitemp-${mac1//:}"

raspi-config nonint do_hostname "$hostname"
hostname -b "$hostname"
systemctl restart avahi-daemon
