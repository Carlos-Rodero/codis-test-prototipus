import machine
import pycom
import time
from micropyGPS import MicropyGPS
from machine import RTC, I2C
from machine import SD
import os


""" SET UP """

# Heartbeat LED flashes in blue colour once every 4s to signal that the system
# is alive. Turn off firmware blinking
pycom.heartbeat(False)

time_searching_GPS = 60

data_gps = {}
data_gps['latitude'] = None
data_gps['longitude'] = None
data_gps['altitude'] = None
data_gps['hdop'] = None

# declare colour leds
led_off = 0x000000
led_green = 0x007f00

pycom.rgbled(led_green)
time.sleep_ms(1000)
pycom.rgbled(led_off)

# RTC
rtc = RTC()

# SD
sd = SD()
os.mount(sd, '/sd')

# check the content
# os.listdir('/sd')

""" FUNCTIONS """


def get_lat_lon_datetime_gps(time_searching_GPS):
    """Obtain latitude and longitude values from GPS

    Parameters
    ----------
    time_searching_GPS: int
        Seconds for searching the GPS

    Return
    ------
    dict
        Dictionary with GPS values

    """
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
        data has been parsed successfully. If so, copies it over to global
        last_data.
        '''
        if gps.satellite_data_updated() and gps.valid:

            timestamp_list = gps.timestamp
            time = (timestamp_list[0], timestamp_list[1],
                    int(timestamp_list[2]), 0, 0)

            date_list = gps.date
            date = (2000 + date_list[2], date_list[1], (date_list[0]))

            datetime = tuple(date) + tuple(time)
            date_std = "{}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}.{}+00:00".format(
                datetime[0], datetime[1], datetime[2],
                datetime[3], datetime[4], datetime[5],
                datetime[6])

            lat = gps.latitude_string()
            lon = gps.longitude_string()
            alt = gps.altitude
            hdop = gps.hdop

            last_data['datetime'] = date_std
            last_data['latitude'] = lat
            last_data['longitude'] = lon
            last_data['altitude'] = alt
            last_data['hdop'] = hdop

            if (last_data['datetime'] is not 0) and \
               (last_data['latitude'] is not 0) and \
               (last_data['longitude'] is not 0):
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

    if ('latitude' in last_data) and ('longitude' in last_data) \
       and ('datetime' in last_data):
        i2c.deinit()
        print(last_data)
        return last_data
    else:
        last_data['datetime'] = 0
        last_data['latitude'] = 0
        last_data['longitude'] = 0
        last_data['altitude'] = 0
        last_data['hdop'] = 0
        i2c.deinit()
        print(last_data)
        return last_data


""" CODE """


for i in range(100000):
    time.sleep_ms(1000)
    data_gps = get_lat_lon_datetime_gps(time_searching_GPS)
    print("latitude: {}, longitude: {}, datetime: {}".format(
        data_gps['latitude'], data_gps["longitude"], data_gps["datetime"]))

    f = open('/sd/gps.txt', 'a')
    f.write("latitude: {}, longitude: {}, datetime: {}".format(
        data_gps['latitude'], data_gps["longitude"], data_gps["datetime"]))
    f.write("\n")
    f.close()
