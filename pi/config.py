#!/usr/bin/env python
import socket

def getlocation():
	# Hostname is like rpi-t-location
	return socket.gethostname()[6:]

general = {
	'location' : getlocation(),
}

mysql = {
	'enabled': True,
	'host': '%MYSQL_HOST%',
	'user': '%MYSQL_USER%',
	'password': '%MYSQL_PASSWORD%',
	'database': 'temperatures'
}

influxdb = {
	'enabled': True,
	'host': '192.168.100.11',
	'port': '8086',
	'user': 'pi01',
	'password': 'raspberry',
	'database': 'temperatures',
	'measurement': 'denieuwezaak'
}
