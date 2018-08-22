from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.resolution = (3280,2464)

camera.start_preview(fullscreen=False, window=(10,50,600,450))

for i in range(5):
    sleep(2)
    camera.capture('/home/pi/Desktop/still%s.jpg' % i)
    
camera.stop_preview()
