from machine import Pin
import time

# declare pin_name
pin_name = 'P9'

# initialize pin in gpio mode and make it an output
p_out = Pin(pin_name, mode=Pin.OUT)

# blink external led for 3 times
for i in range(3):
    p_out.value(1)
    time.sleep(1)
    p_out.value(0)
    time.sleep(1)
