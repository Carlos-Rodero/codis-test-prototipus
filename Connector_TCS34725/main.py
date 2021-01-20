from machine import I2C
import pycom
import time

pycom.heartbeat(False)

# SDA and SCL pins
SDA_pin = 'P11'
SCL_pin = 'P21'


def read_TCS34725_sensors():
    """
    Function to read light values from each sensor connected to I2C.
    Create the sensors list with this values.

    """
    # to avoid errors in sipy, we need to import tcs34725 lib on this part of the code
    import tcs34725

    i2c = I2C(0, pins=(SDA_pin, SCL_pin))

    sensor = tcs34725.TCS34725(i2c)
    # set integration time as integration_time_TCS34725
    # sensor.integration_time(value=integration_time_TCS34725)
    # and gain as gain_TCS34725
    # sensor.gain(gain_TCS34725)
    red, green, blue, clear = sensor.read(raw=True)
    print("red:{}, green:{}, blue:{}, clear:{}".format(red, green, blue, clear))


read_TCS34725_sensors()
