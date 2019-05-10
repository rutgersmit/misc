#!/usr/bin/env python
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
	'measurement': 'denieuwezaak',# think of measurement as a SQL table, it's not... but...
	'location': 'office'
}
