import socket
#import threading

PORT = 2603

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', PORT))

print socket.gethostname()

def main():
	serversocket.listen(5)
	while 1:
		(clientsocket, address) = serversocket.accept()
		provide_task(clientsocket)
		clientsocket.close()

def provide_task(s):
	a = s.recv(2048)
	print a

main()