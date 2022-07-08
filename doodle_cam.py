from picamera import PiCamera
from time import sleep
from datetime import datetime as dt

camera=PiCamera()

camera.start_preview()

for i in range(3):
	sleep(5)
	camera.capture('./photos/%s_doodle.jpg'%dt.now().strftime("%Y%m%d_%H%M%S"))
camera.stop_preview()
