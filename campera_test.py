from picamera import PiCamera
from time import sleep

camera=PiCamera()

camera.start_preview()

sleep(5)
camera.capture('./photos/p2.jpg')
for i in range(5):
	sleep(5)
	camera.capture('./photos/image%s.jpg'%i)
camera.stop_preview()
