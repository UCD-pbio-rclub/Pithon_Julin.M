# time lapse image capture

#pretty much copied from https://picamera.readthedocs.io/en/release-1.13/recipes1.html#capturing-timelapse-sequences

from picamera import PiCamera
from time import sleep

delay = 10 #in seconds

camera = PiCamera()
camera.rotation = 180
camera.resolution = (3280,2464)
camera.start_preview(fullscreen=False, window=(10,50,600,450))

try:
    for filename in camera.capture_continuous('/home/pi/Desktop/img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        sleep(delay) # 
finally:
    camera.stop_preview()
