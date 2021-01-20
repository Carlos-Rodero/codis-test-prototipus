from machine import SD
import os

sd = SD()
os.mount(sd, '/sd')

# check the content
os.listdir('/sd')

# try some standard file operations
f = open('/sd/test.txt', 'w')
f.write('Testing SD card write operations 5')
f.close()
f = open('/sd/test.txt', 'r')
print(f.read())
f.close()
