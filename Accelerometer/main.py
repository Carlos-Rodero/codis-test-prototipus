from LIS2HH12 import LIS2HH12
from pytrack import Pytrack
import time


py = Pytrack()
# init accelerometer
acc = LIS2HH12()

# print pitch and roll for 100 times
for i in range(100):
    pitch = acc.pitch()
    roll = acc.roll()
    print('pitch: {}, roll: {}'.format(pitch, roll))
    time.sleep_ms(100)
