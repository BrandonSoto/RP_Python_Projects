from gpiozero import LED
from time import sleep

SLEEP_TIME = .25 # 250 milliseconds 

red_led = LED( 23 )
blue_led = LED( 16 )
green_led = LED( 17 )

led_list = ( red_led, blue_led, green_led )

for i in range( 0, 10 ):
    for j in range( 0, len( led_list ) ):
        led_list[j].on()
        sleep( SLEEP_TIME )
        led_list[j].off()

print( 'Done!' )
