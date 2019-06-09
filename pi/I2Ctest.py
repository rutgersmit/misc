#!/usr/bin/env python
import smbus
bus = smbus.SMBus(1) 

def device_present():
    for device in range(128):
        try:
            bus.read_byte(device)
            return true
#            print(hex(device))
        except:
            continue

    return false
