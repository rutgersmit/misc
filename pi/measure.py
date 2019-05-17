#! /usr/bin/env python
import sys
import time
import signal
import datetime
import threading
import mysql.connector
import config as cfg

from influxdb import InfluxDBClient
from ds18b20 import DS18B20

def save_mysql(timestamp, location, temperature, humidity):
	if cfg.mysql['enabled'] == False:
		print "Saving to MySQL is disabled in the config"
		return

	sys.stdout.write("Saving to MySQL...")
	sys.stdout.flush()

	tsql = """INSERT INTO `temperatures` (`datetime`, `location`, `temperature`, `humidity`) VALUES(%s,%s,%s,%s);"""
	insert = (timestamp, location, temperature, humidity)

	#connection = mysql.connector.connect(host='\''+cfg.mysql['host']+'\'',database='\''+cfg.mysql['database']+'\'',user='\''+cfg.mysql['user']+'\'',password='\''+cfg.mysql['password']+'\'')
	connection = mysql.connector.connect(host=cfg.mysql['host'],database=cfg.mysql['database'],user=cfg.mysql['user'],password=cfg.mysql['password'])
	cursor = connection.cursor(prepared=True)

	result = cursor.execute(tsql, insert)

	connection.commit()
	connection.close()
	sys.stdout.write(" done!\n")
	sys.stdout.flush()


def save_influxdb(timestamp, location, temperature, humidity):
	if cfg.influxdb['enabled'] == False:
		print "Saving to InfluxDB is disabled in the config"
		return

	sys.stdout.write("Saving to InfluxDB...")
	sys.stdout.flush()
	influx_data = [
			{
				"measurement": cfg.influxdb['measurement'],
				"tags": {
					"location": location,
				},
				"time": timestamp,
				"fields": {
					"temperature" : temperature,
					"humidity": humidity
				}
			}
		]

	influx_client = InfluxDBClient(host='\''+cfg.influxdb['host']+'\'', port=cfg.influxdb['port'], username='\''+cfg.influxdb['user']+'\'', password='\''+cfg.influxdb['password']+'\'', database='\''+cfg.influxdb['database']+'\'')
	influx_client.write_points(influx_data)

	sys.stdout.write(" done!\n")
	sys.stdout.flush()


def measure():

	try:
		# Read the sensor using the configured driver and gpio
		timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
		loc = cfg.general['location'];

		sensor = DS18B20()

		temperature = sensor.tempC(0)
		if  temperature > 100: # mis read
			temperature = sensor.tempC(0)
		humidity = 0.0

		# Print for debugging, uncomment the below line
		sys.stdout.write("[%s]- %s - Temp: %s, Humidity: %s\n" % (timestamp, loc, temperature, humidity))
		sys.stdout.flush()

		# Save to InfluxDB
		try:
			save_influxdb(timestamp, loc, temperature, humidity)
		except Exception, e:
			print "Error saving to InfluxDB: " + str(e.message)


		# Save to MySQL
		try:
			save_mysql(timestamp, loc, temperature, humidity)
		except Exception, e:
			print "Error saving to MySQL: " + str(e.message)


	except KeyboardInterrupt:
		pass


if __name__ == "__main__":
	measure()
