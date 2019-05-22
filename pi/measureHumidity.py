#!/usr/bin/python
import sys
import array
import operator
import Adafruit_DHT

measurecount=10
temps = [0 for i in xrange(measurecount)]
humids = [0 for i in xrange(measurecount)]

def Average(lst):
    lst=filter(operator.isNumberType, lst) # remove non numeric values
    lst.remove(max(lst)) # remove one highest value
    lst.remove(min(lst)) # remove one lowest value
    return sum(lst) / len(lst) # return the average

def gethumidity():
    for x in range(measurecount):
        humidity, temperature = Adafruit_DHT.read(11, 2)
        if humidity is None or temperature is None:
#            print 'No DHT11 sensor found'
            temps[x] = 'x'
            humids[x] = 'x'
        else:
#            print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
            temps[x] = temperature
            humids[x] = humidity

    return round(Average(humids),2)
