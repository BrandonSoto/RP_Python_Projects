import RPi.GPIO as GPIO
import time

SLEEP_TIME = .25 # 250 milliseconds 

red_led = 11
blue_led = 18
green_led = 32

led_list = [red_led, blue_led, green_led]

GPIO.setmode( GPIO.BOARD )
GPIO.setup( led_list, GPIO.OUT )
GPIO.setwarnings( False )

for i in range( 0, 10 ):
    GPIO.output( led_list, (GPIO.HIGH, GPIO.LOW, GPIO.LOW) )
    time.sleep( SLEEP_TIME )
    GPIO.output( led_list, (GPIO.LOW, GPIO.HIGH, GPIO.LOW) )
    time.sleep( SLEEP_TIME )
    GPIO.output( led_list, (GPIO.LOW, GPIO.LOW, GPIO.HIGH) )
    time.sleep( SLEEP_TIME )

GPIO.cleanup();
print( 'Done!' )
