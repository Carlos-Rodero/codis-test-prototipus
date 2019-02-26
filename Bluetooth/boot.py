import os
import machine

sd = machine.SD()
os.mount(sd, '/sd')