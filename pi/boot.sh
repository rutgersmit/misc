#!/bin/bash
files=( "ds18b20.py" "config.py" "measure.py" "measureHumidity.py" "measureTemperatureSW.py" "measureTemperatureI2C.py")
for i in "${files[@]}"
do
	wget -q https://raw.githubusercontent.com/rutgersmit/misc/master/pi/$i -o /home/pi/$i
done
