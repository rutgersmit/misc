#!/usr/bin/env python
import socket

def getlocation():
	# Hostname is like rpi-t-location
	return socket.gethostname()[6:]

general = {
	'location' : getlocation(),
}

mysql = {
	'host': '192.168.100.200',
	'user': 'temperatures',
	'password': 'temperatures',
	'database': 'temperatures'
}

influxdb = {
	'host': '192.168.100.11',
	'port': '8086',
	'user': 'pi01',
	'password': 'raspberry',
	'database': 'temperatures',
	'measurement': 'denieuwezaak'
}
