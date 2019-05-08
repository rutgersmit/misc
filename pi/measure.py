#! /usr/bin/env python
import sys
import time
import signal
import datetime
import threading

import mysql.connector

from influxdb import InfluxDBClient
from ds18b20 import DS18B20



# Configure Azure SQL connction variables
sql_host = "rutger-mysql-svr.mysql.database.azure.com"
sql_host = "192.168.100.200"
sql_database = "temperatures"
sql_user = "temperatures"
sql_password = "temperatures"

import mysql.connector


# Configure InfluxDB connection variables
influx_host = "192.168.100.11" # influx server
influx_port = 8086 # default port
influx_user = "pi01"
influx_password = "raspberry"
influx_dbname = "temperatures"

interval = 60 # Sample period in seconds

influx_client = InfluxDBClient(influx_host, influx_port, influx_user, influx_password, influx_dbname)

# think of measurement as a SQL table, it's not...but...
measurement = "rpi-dht11"
# location will be used as a grouping tag later
location = "office"

def measure():
	# Run until you get a ctrl^c
	try:
		# Read the sensor using the configured driver and gpio
		timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

		x = DS18B20()
		count = x.device_count()
		i = 0

		#print("Sensors: %s" % count)

		temperature = x.tempC(0)
		if  temperature > 100: # mis read
			temperature = x.tempC(0)
		humidity = 0.0

		# Print for debugging, uncomment the below line
		sys.stdout.write("[%s]- %s - Temp: %s, Humidity: %s\n" % (timestamp, location, temperature, humidity))

		# Create the JSON data structure
		influx_data = [
				{
					"measurement": measurement,
					"tags": {
						"location": location + "-" + str(i),
					},
					"time": timestamp,
					"fields": {
						"temperature" : temperature,
						"humidity": humidity
					}
				}
			]

		# Send the JSON data to InfluxDB
		sys.stdout.write("Saving to MySQL...")

		tsql = """INSERT INTO `temperatures` (`datetime`, `location`, `temperature`, `humidity`) VALUES(%s,%s,%s,%s);"""
		insert = (timestamp, location, temperature, humidity)

		connection = mysql.connector.connect(host=sql_host,database=sql_database,user=sql_user,password=sql_password)
		cursor = connection.cursor(prepared=True)

		result = cursor.execute(tsql, insert)

		connection.commit()
		connection.close()
		sys.stdout.write(" done!\n")


		sys.stdout.write("Saving to InfluxDB...")
		influx_client.write_points(influx_data)

		sys.stdout.write(" done!\n")
		sys.stdout.flush()


	except KeyboardInterrupt:
		pass


if __name__ == "__main__":
	measure()
