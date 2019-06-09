#!/usr/bin/python
import sys
import array
import operator
import Adafruit_DHT

measurecount=10
temps = [0] * measurecount
humids = [0] * measurecount

def Average(lst):
    lst=filter(operator.isNumberType, lst) # remove non numeric values
    if len(lst) == 0:
        return 0

    lst.remove(max(lst or [0])) # remove one highest value
    if len(lst) < 3:
        return 0

    lst.remove(min(lst or [0])) # remove one lowest value
    if len(lst) < 3:
        return 0

    return sum(lst) / len(lst) # return the average

def readHumidity():
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


if __name__=="__main__":
   h = readHumidity()
   print "Humidity: ", h