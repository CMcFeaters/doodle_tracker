from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
from datetime import datetime as dt
import cv2
import socket
import numpy as np
import os

HOST = "192.168.1.9"	#basic loopback for local host
PORT=65432	#non-privileged port

camera=PiCamera()


while True:	#eternal loop
	#take the pictures
	sleep(600)
	camera.start_preview()
	sleep(2)
	rawdata=PiRGBArray(camera)	#RGB array object
	camera.capture(rawdata,'bgr')
	camera.stop_preview()
	print('Captured %dx%d image'%(rawdata.array.shape[1],rawdata.array.shape[0]))

	#process the image
	image=rawdata.array
	encoded=cv2.imencode('.jpg',image)[1]

	#send over socket
	print("starting")
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print("connecting")
		s.connect((HOST,PORT))
		s.sendall(encoded)

