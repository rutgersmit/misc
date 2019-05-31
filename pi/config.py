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
	'host': '%INFLUX_HOST%',
	'port': '%INFLUX_PORT%',
	'user': '%INFLUX_USER%',
	'password': '%INFLUX_PASSWORD%',
	'database': 'temperatures',
	'measurement': 'denieuwezaak'
}
