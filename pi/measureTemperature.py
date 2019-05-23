#!/usr/bin/python
import sys
from ds18b20 import DS18B20

def gettemperature():
    sensor = DS18B20()
    t = sensor.tempC(0)
    if  t > 100: # mis read
        t = sensor.tempC(0)
    return t
