import machine
import time
from machine import UART
import pycom


# Heartbeat LED flashes in blue colour once every 4s to signal that the system
# is alive. Turn off firmware blinking
pycom.heartbeat(False)

# declare colour leds
led_off = 0x000000
led_green = 0x007f00


def led():
    pycom.rgbled(led_green)
    time.sleep_ms(1000)
    pycom.rgbled(led_off)


# init UART. LEDS because pins are in REPL and we need to know everything is OK
led()
uart = UART(0, 115200)
led()
uart.init(115200, bits=8, parity=None, stop=1, pins=('P1', 'P0'))


time_waiting_UART = 20
message = "test"


def set_UART_message(data=None):
    """
    Set messages to UART
    """
    data_UART = "D" + str(data)
    uart.write(data_UART)
    time.sleep_ms(100)


def get_UART_message():
    """
    Get messages from UART
    """
    chrono = machine.Timer.Chrono()
    chrono.start()
    val = 1
    while True:
        # read some data from UART
        if (uart.any() > 0):
            val = uart.read().strip()

        elapsed = chrono.read()

        if elapsed > time_waiting_UART:
            return val


for i in range(5):
    # Read and set message from UART during 5 times
    time.sleep_ms(1000)
    led()
    set_UART_message(message)
    try:
        message = get_UART_message().decode('Ascii')
        message += str(i)
    except Exception as er:
        message = "no message"
