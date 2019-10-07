from machine import Pin
import pycom
import time

pycom.heartbeat(False)

# declare pin_name
pin_name = 'P23'

# declare colour leds
led_off = 0x000000
led_green = 0x007f00

# initialize pin in gpio mode and make it an output
p_out = Pin(pin_name, mode=Pin.OUT)

# blink external led for 3 times
for i in range(2):
    p_out.value(1)
    pycom.rgbled(led_green)
    time.sleep(4)
    p_out.value(0)
    pycom.rgbled(led_off)
    time.sleep(4)
