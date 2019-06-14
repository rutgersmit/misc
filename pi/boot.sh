#!/bin/bash
rfkill unblock all
apt install python-smbus -y

files=( "ds18b20.py" "config.py" "measure.py" "measureHumidity.py" "measureTemperatureSW.py" "measureTemperatureI2C.py")
for i in "${files[@]}"
do
        echo 'Download ' $i
        wget https://raw.githubusercontent.com/rutgersmit/misc/master/pi/$i -O /home/pi/$i
done
