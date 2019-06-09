import board
import digitalio
import busio
import time
import adafruit_bme280

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

def gettemperature():
    return bme280.temperature

def gethumidity():
    return bme280.humidity

def getpressure():
    return bme280.pressure

def getaltitude():
    return bme280.altitude