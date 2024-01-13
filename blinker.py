import utime
from machine import Pin

# Configure led pin
BUILD_IN_LED_PIN = 25
led_onboard = Pin(BUILD_IN_LED_PIN, Pin.OUT)

class Led:
    """ Using this class you can access onboard led quickly """

    def switch(z: bool):
        """ This function will turn on or off the led """
        if z == 1:
            led_onboard.on()
        else:
            led_onboard.off()

    def blink(delay: float, off_delay=True):
        """ This function will turn on for given time and turn off the led after that """
        self.switch(1)
        utime.sleep(delay)
        self.switch(0)
        if off_delay == True:
            utime.sleep(delay)
        else: pass

    def loop(interval: float):
        while True:
            self.blink(interval)