#camera pushbutton

from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
switch_pin = 21
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

camera = PiCamera()
camera.rotation = 180
camera.resolution = (3280,2464)
camera.start_preview(fullscreen=False, window=(10,50,600,450))

i = 1

try:
    while True:
        if GPIO.input(switch_pin) == False:
            print('capturing image ' + str(i))
            filename = '/home/pi/Desktop/img' + str(i) + ".jpg"
            camera.capture(filename)
            i += 1
        sleep(0.2)
finally:
    camera.stop_preview()
    
        


