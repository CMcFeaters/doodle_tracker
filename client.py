# basic socket test client

import socket
import tqdm
import os

HOST = "127.0.0.1"	#basic loopback for local host
PORT=65432	#non-privileged port

print("starting")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	f=open(r'.\photos\20220709_064506_doodle.jpg','rb')
	l=os.path.getsize(r'.\photos\20220709_064506_doodle.jpg')
	print(l)
	print("connecting")
	s.connect((HOST,PORT))
	print("Sending")

	i=0
	dat=f.read(l)
	'''while dat:
		print("sending %d"%i)
		s.send(dat)
		dat=f.read(1024)
		i+=1
	'''
	s.sendall(dat)
	#print("receiving")
	#data=s.recv(1024)
	
print("Done")