#!/usr/bin/python
import sys
import array

import Adafruit_DHT



def Average(lst):
    return sum(lst) / len(lst)


measurecount=10
temps = [0 for i in xrange(measurecount)]
humids = [0 for i in xrange(measurecount)]

for x in range(measurecount):
    print '.'

#    humidity, temperature = Adafruit_DHT.read_retry(11, 3)
    humidity, temperature = Adafruit_DHT.read(11, 2)
    if humidity is None or temperature is None:
        temps.pop(x)
        humids.pop(x)
        print 'No DHT11 sensor found'
    else:
        temps[x] = temperature
        humids[x] = humidity
        print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)


print "Average: ", round(Average(temps),2)
print "Humidity: ", round(Average(humids),2)
