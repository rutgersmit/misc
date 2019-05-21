#!/usr/bin/python
import sys
import array
import operator
import Adafruit_DHT

def Average(lst):
    lst=filter(operator.isNumberType, lst)
    return sum(lst) / len(lst)

measurecount=10
temps = [0 for i in xrange(measurecount)]
humids = [0 for i in xrange(measurecount)]

for x in range(measurecount):
    humidity, temperature = Adafruit_DHT.read(11, 2)
    if humidity is None or temperature is None:
        print 'No DHT11 sensor found'
        temps[x] = 'x'
        humids[x] = 'x'
    else:
        print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
        temps[x] = temperature
        humids[x] = humidity

print "Average: ", round(Average(temps),2)
print "Humidity: ", round(Average(humids),2)
