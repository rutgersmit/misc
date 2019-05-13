#! /usr/bin/env python
import sys
import mysql.connector

import config as cfg

from influxdb import InfluxDBClient

connection = mysql.connector.connect(host=cfg.mysql['host'],database=cfg.mysql['database'],user=cfg.mysql['user'],password=cfg.mysql['password'])
cursor = connection.cursor(prepared=True)

tsql =('CREATE TABLE IF NOT EXISTS temperatures ('
    'id INT AUTO_INCREMENT, '
    'datetime DATETIME, '
    'location VARCHAR(50) NOT NULL, '
    'temperature DECIMAL(4,2), '
    'humidity DECIMAL(4,2), '
    'PRIMARY KEY (id)'
');')
mysqlresult = cursor.execute(tsql)
connection.commit()
connection.close()

print "=== MySQL result ==="
print mysqlresult
print "====================="
print "."

influx_client = InfluxDBClient(cfg.influxdb['host'], cfg.influxdb['port'], cfg.influxdb['user'], cfg.influxdb['password'])
influxresult = influx_client.create_database(cfg.influxdb['database'])

print "=== Influx result ==="
print influxresult
print "====================="