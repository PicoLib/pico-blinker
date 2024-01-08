import utime
from machine import Pin

BUILD_IN_LED_PIN = 25
led_onboard = Pin(BUILD_IN_LED_PIN, Pin.OUT)

def blink_led_loop(x):
    while True:
        led_onboard.on()
        utime.sleep(x)
        led_onboard.off()
        utime.sleep(x)

def blink_led(y):
    led_onboard.on()
    utime.sleep(y)
    led_onboard.off()
    utime.sleep(y)

def led(z):
    if z == 1:
        led_onboard.on()
    else:
        led_onboard.off()
