import time
import board
import digitalio

# Setup the onboard LED
onboard_led = digitalio.DigitalInOut(board.LED)
onboard_led.direction = digitalio.Direction.OUTPUT

pin_step = digitalio.DigitalInOut(board.D8)
pin_step.direction = digitalio.Direction.OUTPUT

pin_direction = digitalio.DigitalInOut(board.D7)
pin_direction.direction = digitalio.Direction.OUTPUT


i = 1

# Blink the LEDs
while True:
    time.sleep(0.002)  # Delay for 0.1 seconds
    pin_step.value = not pin_step.value
    i += 1
    if i % 200 == 0:
        pin_direction.value = not pin_direction.value
        onboard_led.value = not onboard_led.value
        print("Change direction")
