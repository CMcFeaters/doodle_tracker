#basic socket test server

import socket
import tqdm
import os

HOST = "127.0.0.1"	#basic loopback for local host
PORT=65432	#non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:	#AF_INET = AddressFamily Internet (IPV4), SOCK_STREAM = TCP
	s.bind((HOST,PORT))
	s.listen()	#bind and listen on the port we initiated
	
	print("waiting")
	conn,add = s.accept()	#accept our connection and address of what we accepted, the program blocks on this line to a connection is received
	print("accepting")
	
	f=open(r'.\photos\recieved.jpg','wb')
	with conn:
		print(f"connected by {add}")
		data=True
		i=0
		data=conn.recv(1024)	#our buffer is 1024 bits
		while data:
			print("writing file %d"%i)
			f.write(data)
			data=conn.recv(1024)
			i+=1
		print("Closed")
		f.close()
		conn.sendall("recieved file")		#echo that back
	print("done")
	

