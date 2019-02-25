from machine import SD
import os

# check the content
os.listdir('/sd')

# try some standard file operations
f = open('/sd/test.txt', 'w')
f.write('Testing SD card write operations')
f.close()
f = open('/sd/test.txt', 'r')
print(f.readall())
f.close()