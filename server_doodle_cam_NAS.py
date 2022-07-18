from time import sleep
from datetime import datetime as dt
import cv2
import socket
import numpy as np
import os

HOST = "192.168.1.9"	#Pi address
PORT=65432	#non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:	#AF_INET = AddressFamily Internet (IPV4), SOCK_STREAM = TCP
	s.bind((HOST,PORT))
	s.listen()	#bind and listen on the port we initiated
	
	i=0
	while True:
		print("waiting")
		conn,add = s.accept()	#accept our connection and address of what we accepted, the program blocks on this line to a connection is received
		print("accepting from ",add)

		with conn:
		#eternally receive
			print("connected to by %s"%str(add))
			i+=1
			tdata=True
			data=0
			data=conn.recv(1024)	#our buffer is 1024 bits
			while tdata:
				tdata=conn.recv(1024)
				data+=tdata
				
				#file is received, now write
			print("File %d received"%i)
			encoded_array=np.fromstring(data,np.uint8)	#convert from string to array
			decoded_image=cv2.imdecode(encoded_array,cv2.IMREAD_COLOR)	#decode arryay to image
			st1=('/mnt/raid1/shared/doodle/%s_doodle.jpg'%dt.now().strftime("%Y%m%d_%H%M%S"))	#file location
			cv2.imwrite(st1,decoded_image)	#write teh file
			print("File %s written"%st1)

