from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
from datetime import datetime as dt
import cv2
import socket
import numpy as np


camera=PiCamera()
rawdata=PiRGBArray(camera)	#RGB array object

#camera.start_preview()
for i in range(2):
	sleep(5)
	camera.capture(rawdata,'rgb')
	print('Captured %dx%d image'%(rawdata.array.shape[1],rawdata.array.shape[0]))
	image=rawdata.array
	encoded=cv2.imencode('.jpg',image)[1]

	encoded_array=np.fromstring(encoded,np.uint8)
	decoded_image=cv2.imdecode(encoded_array,cv2.IMREAD_COLOR)
	#camera.capture('./photos/%s_doodle.jpg'%dt.now().strftime("%Y%m%d_%H%M%S"))
	cv2.imwrite('./photos/test%s.jpg'%i,decoded_image)

	#camera.stop_preview()
