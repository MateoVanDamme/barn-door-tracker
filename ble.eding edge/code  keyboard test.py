import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize the USB HID keyboard
kbd = Keyboard(usb_hid.devices)


# while(True):
#     # Delay before sending the keystroke (in seconds)
#     delay = 1
#     # Wait fdor the specified delay
#     time.sleep(delay)
#     # Send the 'd' key press
#     kbd.press(Keycode.D)
#     kbd.release_all()
