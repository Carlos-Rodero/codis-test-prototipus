import machine
from machine import I2C
from pytrack import Pytrack
import pycom
import time

# disable heartbeat
pycom.heartbeat(False)

# color leds
led_red = 0x7f0000
led_green = 0x007f00
led_yellow = 0x7f7f00
led_blue = 0x00FFFF
led_orange = 0xFF9900
led_pink = 0xFF00FF

# time values in seconds of different variables
time_to_deep_sleep = 60


def blink_led(times, ms, color):
    """ Function to uses the RGB LED to make a blink light

    Parameters
    ----------
        times: int
            number of times to blink the light.
        ms: int
            time in ms that will be blink the light
        color: string
            type of color
    """
    for cycles in range(times):
        pycom.rgbled(color)
        time.sleep_ms(int(ms/2))
        pycom.heartbeat(False)
        time.sleep_ms(int(ms/2))


def deep_sleep(time_to_deep_sleep):
    """
    Function to set Pytrack in ultra low power (deep sleep) during x time.

    Parameters
    -------
        time_to_deep_sleep: int
            seconds to stay in deep sleep
    """
    i2c = machine.I2C(0, mode=I2C.MASTER, pins=('P22', 'P21'))
    py = Pytrack(i2c=i2c)
    py.setup_sleep(time_to_deep_sleep)
    py.go_to_sleep(gps=True)
    i2c.deinit()


blink_led(1, 1000, led_green)
time.sleep_ms(10000)
print("a punt entrar while")
while True:
    # Enter to deep sleep. LED red
    time.sleep_ms(1000)
    blink_led(2, 1000, led_red)
    print("entra deep sleep")
    time.sleep_ms(1000)
    deep_sleep(time_to_deep_sleep)
    print('fa deep sleep')
