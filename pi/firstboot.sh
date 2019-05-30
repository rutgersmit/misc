apt update
apt install python-dev python-setuptools git -y
git clone https://github.com/adafruit/Adafruit_Python_DHT
cd Adafruit_Python_DHT
python setup.py install
cd ..
rm -rf Adafruit_Python_DHT
