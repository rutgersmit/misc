PERCENTAGE=5

{
chmod 755 /boot/PiBakery/blocks/downloadfile/downloadFile.sh >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 1 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
/boot/PiBakery/blocks/downloadfile/downloadFile.sh https://raw.githubusercontent.com/rutgersmit/misc/master/pi/boot.sh /home/pi/startup.sh >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 2 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
chmod 755 /boot/PiBakery/blocks/downloadfile/downloadFile.sh >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 3 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
/boot/PiBakery/blocks/downloadfile/downloadFile.sh https://raw.githubusercontent.com/rutgersmit/misc/master/pi/ds18b20.py /home/pi/ds18b20.py >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 4 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
chmod 755 /boot/PiBakery/blocks/downloadfile/downloadFile.sh >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 5 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
/boot/PiBakery/blocks/downloadfile/downloadFile.sh https://raw.githubusercontent.com/rutgersmit/misc/master/pi/config.py /home/pi/config.py >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 6 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
chmod 755 /boot/PiBakery/blocks/downloadfile/downloadFile.sh >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 7 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
/boot/PiBakery/blocks/downloadfile/downloadFile.sh https://raw.githubusercontent.com/rutgersmit/misc/master/pi/measure.py /home/pi/measure.py >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 8 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
chmod 755 /boot/PiBakery/blocks/downloadfile/downloadFile.sh >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 9 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
/boot/PiBakery/blocks/downloadfile/downloadFile.sh https://raw.githubusercontent.com/rutgersmit/misc/master/pi/measureHumidity.py home/pi/measureHumidity.py >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 10 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
chmod 755 /boot/PiBakery/blocks/downloadfile/downloadFile.sh >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 11 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
/boot/PiBakery/blocks/downloadfile/downloadFile.sh https://raw.githubusercontent.com/rutgersmit/misc/master/pi/measureTemperature.py home/pi/measureTemperature.py >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 12 )
echo "\nProcessing Every Boot Script\n\nRunning Block: downloadfile"
echo XXX
chmod 755 /boot/PiBakery/blocks/runcommand/runCommand.sh >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 13 )
echo "\nProcessing Every Boot Script\n\nRunning Block: runcommand"
echo XXX
/boot/PiBakery/blocks/runcommand/runCommand.sh "chmod +x /home/pi/startup.sh" root >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 14 )
echo "\nProcessing Every Boot Script\n\nRunning Block: runcommand"
echo XXX
chmod 755 /boot/PiBakery/blocks/runcommand/runCommand.sh >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 15 )
echo "\nProcessing Every Boot Script\n\nRunning Block: runcommand"
echo XXX
/boot/PiBakery/blocks/runcommand/runCommand.sh /home/pi/startup.sh root >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 16 )
echo "\nProcessing Every Boot Script\n\nRunning Block: runcommand"
echo XXX
chmod 755 /boot/PiBakery/blocks/runcommand/runCommand.sh >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 17 )
echo "\nProcessing Every Boot Script\n\nRunning Block: runcommand"
echo XXX
/boot/PiBakery/blocks/runcommand/runCommand.sh "sed -i -e 's/%MYSQL_HOST%/192.168.0.24/g' -e 's/%MYSQL_USER%/temperatures/g' -e 's/%MYSQL_PASSWORD%/VN3tXuLaPpY6Nk7f6w2CV4qd/g' -e 's/%INFLUX_HOST%/192.168.0.24/g' -e 's/%INFLUX_PORT%/8086/g' -e 's/%INFLUX_USER%/temperatures/g' -e 's/%INFLUX__PASSWORD%/temperatures/g' /home/pi/config.py" root >>/boot/PiBakery/everyboot.log 2>&1  || true
echo XXX
echo $(expr $PERCENTAGE \* 18 )
echo "\nProcessing Every Boot Script\n\nRunning Block: runcommand"
echo XXX
echo 100
} | whiptail --title "PiBakery" --gauge "\nProcessing Every Boot Script\n\n\n" 11 40 0
