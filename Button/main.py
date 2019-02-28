from machine import Pin, Timer
import pycom
import time

# disable heartbeat
pycom.heartbeat(False)

# declare colour leds
led_off = 0x000000
led_green = 0x007f00

# declare pin_name
pin_name = 'P14'

# timeout
timeout_secs = 10

# start a timer
chrono = Timer.Chrono()
chrono.start()

while True:
    if Pin('P14').value() == 0:
        pycom.rgbled(led_green)
    else:
        pycom.rgbled(led_off)

    elapsed = chrono.read()

    if elapsed > timeout_secs:
        break
