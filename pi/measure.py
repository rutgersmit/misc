#! /usr/bin/env python
import sys
import time
import datetime
import mysql.connector

import I2Ctest as i2ctest

import config as cfg
import measureTemperatureI2C as i2cTemp
import measureTemperature as mTemp
import measureHumidity as mHumid

from influxdb import InfluxDBClient

def save_mysql(timestamp, location, temperature, humidity):
    if cfg.mysql['enabled'] == False:
        print "Saving to MySQL is disabled in the config"
        return

    sys.stdout.write("Saving to MySQL...")
    sys.stdout.flush()

    tsql = """INSERT INTO `temperatures` (`datetime`, `location`, `temperature`, `humidity`) VALUES(%s,%s,%s,%s);"""
    insert = (timestamp, location, temperature, humidity)

    connection = mysql.connector.connect(host=cfg.mysql['host'],database=cfg.mysql['database'],user=cfg.mysql['user'],password=cfg.mysql['password'],connection_timeout=5)
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

    influx_client = InfluxDBClient(cfg.influxdb['host'], cfg.influxdb['port'], cfg.influxdb['user'], cfg.influxdb['password'], cfg.influxdb['database'], timeout=5)
    influx_client.write_points(influx_data)

    sys.stdout.write(" done!\n")
    sys.stdout.flush()

if __name__ == "__main__":
    print "Measure temperature"

    if i2ctest.device_present():
        print "Measuring via I2C"
        temperature = i2cTemp.gettemperature()
    else:
        print "Measuring via Single Wire"
        temperature = mTemp.gettemperature()
    
    if temperature == 666:
        print "No temperature/saensor found, exiting"
        sys.exit()

    print "Temperature: ", temperature

    print "Measure humidity"
    if i2ctest.device_present():
        print "Measuring via I2C"
        temperature = i2cTemp.gethumidity()
    else:
        print "Measuring via Single Wire"
        humidity=mHumid.gethumidity()

    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    loc = cfg.general['location'];

    try:
        save_mysql(timestamp, loc, temperature, humidity)
    except:
        print "Error saving to MySQL"
    
    try:
        save_influxdb(timestamp, loc, temperature, humidity)
    except:
        print "Error saving to InfluxDB"
