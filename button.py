from gpiozero import LED, Button
from time import sleep

def pressed( button ):
    if led.value > 0: # led is on
        led.off()
    else:
        led.on()

# GPIO components
led = LED( 17 )
button = Button( 26 )
button.when_pressed = pressed

while input('') != 'q':
    sleep( .5 )

