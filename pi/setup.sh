sh -c "echo 'dtoverlay=w1-gpio' >> /boot/config.txt"
sh -c "echo 'w1-gpio pullup=1' >> /etc/modules"
sh -c "echo 'w1-therm' >> /etc/modules"
sh -c "echo '* * * * * pi /home/pi/measure.py' >> /etc/cron.d/per_minute"
