#!/usr/bin/python

import sys
from ds18b20 import DS18B20

def readTemperature():
  try:
    sensor = DS18B20()
    t = sensor.tempC(0)
    if t > 100: #mis read, try again!
      t = sensor.tempC(0)
    
    return t

  except:
    return 666


if __name__=="__main__":
   t = readTemperature()
   print "Temperature: ", t