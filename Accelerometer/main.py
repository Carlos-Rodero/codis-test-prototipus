from LIS2HH12 import LIS2HH12
from pytrack import Pytrack
import time

py = Pytrack()
acc = LIS2HH12()
for i in range(100):
    pitch = acc.pitch()
    roll = acc.roll()
    print('pitch: {}, roll: {}'.format(pitch, roll))
    time.sleep_ms(100)
