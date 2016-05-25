import socket
import os
import threading

clients = []
end = False
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

def task():
	while True:
		t = raw_input("press Enter to start recording")
		if "exit" in t:
			end = True
			return	
		for c in clients:
			c.send("#")

T = threading.Thread(target=task)
T.start()


host = '0.0.0.0'
print host
port = 9998
s.bind((host,port))
s.listen(5)
recvCount = 0
while end == False:
    c, addr = s.accept()
    clients.append(c)
    print 'Got connection from', addr

for c in clients:
	c.close
s.close()