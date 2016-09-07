from gpiozero import LED
import time

SLEEP_TIME = 1

led = LED(17)
led.on()

while input() != 'q':
    time.sleep(.5)

print( 'Done!' )
