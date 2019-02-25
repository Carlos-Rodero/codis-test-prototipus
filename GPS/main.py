import machine
import pycom
import os
import time
from micropyGPS import MicropyGPS
from pytrack import Pytrack
from machine import RTC, I2C


time_searching_GPS = 30

data_gps = {}
data_gps['latitude'] = None
data_gps['longitude'] = None
data_gps['altitude'] = None
data_gps['hdop'] = None

# Heartbeat LED flashes in blue colour once every 4s to signal that the system is alive
# Turn off firmware blinking
pycom.heartbeat(False)

# RTC
rtc = RTC()

""" FUNCTIONS """


def get_lat_lon_datetime_gps(time_searching_GPS):
    GPS_TIMEOUT_SECS = time_searching_GPS
    # init I2C to P21/P22
    i2c = machine.I2C(0, mode=I2C.MASTER, pins=('P22', 'P21'))
    # write to address of GPS
    GPS_I2CADDR = const(0x10)
    raw = bytearray(1)
    i2c.writeto(GPS_I2CADDR, raw)
    # create MicropyGPS instance. location formatting with commas
    gps = MicropyGPS(location_formatting='dd')
    # start a timer
    chrono = machine.Timer.Chrono()
    chrono.start()
    # store results here
    last_data = {}
    # return from validate coordinates
    res = False

    def check_for_valid_coordinates(gps):
        '''
        Given a MicropyGPS object, this function checks if valid coordinate
        data has been parsed successfully. If so, copies it over to global last_data.
        '''
        if gps.satellite_data_updated() and gps.valid:

            timestamp_list = gps.timestamp
            time = (timestamp_list[0], timestamp_list[1], int(timestamp_list[2]), 0, 0)

            date_list = gps.date
            date = (2000 + date_list[2], date_list[1], (date_list[0]))

            datetime = tuple(date) + tuple(time)

            lat_list = gps.latitude_string().split("°")
            lat = float(lat_list[0])

            lon_list = gps.longitude_string().split("°")
            lon = float(lon_list[0])

            alt = gps.altitude

            hdop = gps.hdop

            last_data['datetime'] = datetime
            last_data['latitude'] = lat
            last_data['longitude'] = lon
            last_data['altitude'] = alt
            last_data['hdop'] = hdop

            if last_data['datetime'] is not 0 and last_data['latitude'] is not 0 and last_data['longitude'] is not 0:
                return True
            else:
                return False

        else:
            return False

    check_for_valid_coordinates(gps)

    while True:
        # read some data from module via I2C
        raw = i2c.readfrom(GPS_I2CADDR, 16)
        # feed into gps object
        for b in raw:
            sentence = gps.update(chr(b))
            if sentence is not None:
                # gps successfully parsed a message from module
                # see if we have valid coordinates
                res = check_for_valid_coordinates(gps)
        elapsed = chrono.read()

        if elapsed > GPS_TIMEOUT_SECS:
            break

    if 'latitude' in last_data and 'longitude' in last_data and 'datetime' in last_data:
        i2c.deinit()
        return last_data
    else:
        last_data['datetime'] = 0
        last_data['latitude'] = 0
        last_data['longitude'] = 0
        last_data['altitude'] = 0
        last_data['hdop'] = 0
        i2c.deinit()
        return last_data


def set_datetime():
    if data_gps['datetime'] is not 0:
        rtc.init(data_gps['datetime'])
    else:
        rtc.init()


""" CODE """

for i in range(100):
    time.sleep_ms(1000)
    data_gps = get_lat_lon_datetime_gps(time_searching_GPS)
    print("latitude: {}, longitude: {}".format(data_gps['latitude'], data_gps["longitude"]))
    set_datetime()
    print(rtc.now())

