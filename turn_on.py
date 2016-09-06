import RPi.GPIO as GPIO
import time

SLEEP_TIME = 1

red_led = 11

GPIO.setmode( GPIO.BOARD )
GPIO.setwarnings( False )
GPIO.cleanup();
GPIO.setup( red_led , GPIO.OUT )

GPIO.output( red_led, GPIO.HIGH )

print( 'changed to on' )

time.sleep( SLEEP_TIME )

GPIO.output( red_led, GPIO.LOW )

print( 'changed to off' )


GPIO.cleanup();
print( 'Done!' )
