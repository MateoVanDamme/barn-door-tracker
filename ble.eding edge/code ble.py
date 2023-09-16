import time
import board
import digitalio
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.button_packet import ButtonPacket
import time
import math
# I/O -----------

# Builtin LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Code --------------

ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

ble.start_advertising(advertisement)


t_now = 0

while True:
    t_now = time.monotonic()
    led.value = (math.floor(2*t_now)) % 2

    ble.start_advertising(advertisement)
    while not ble.connected:
        pass

    # Now we're connected

    while ble.connected:
        if uart.in_waiting:
            packet = Packet.from_stream(uart)
            if isinstance(packet, ButtonPacket):
                if packet.pressed:
                    if packet.button == ButtonPacket.BUTTON_1:
                        # The 1 button was pressed.
                        print("1 button pressed!")
                    elif packet.button == ButtonPacket.UP:
                        # The UP button was pressed.
                        print("UP button pressed!")

    # If we got here, we lost the connection. Go up to the top and start
    # advertising again and waiting for a connection.