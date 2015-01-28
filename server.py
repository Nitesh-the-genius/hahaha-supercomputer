import socket

PORT = 2603

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', PORT))

def main():
    serversocket.listen(5)
    (clientsocket, address) = serversocket.accept()
    while 1:
        provide_task(clientsocket)
    clientsocket.close()

def provide_task(s):
    print "Recieved connection. Sending task."
    task = "r=1+1\n" # Must define r and end with 1010011010
    print s.send(task)
    result = s.recv(2048)
    print "Recieved result. Result is, " , result

main()