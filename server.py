import socket
import threading

PORT = 2603

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', PORT))

def main():
    serversocket.listen(5)
    jobs = []
    for i in range(3):
        p = threading.Thread(target=worker,args=(i,))
        jobs.append(p)
        p.start()

def worker(i):
    (clientsocket, address) = serversocket.accept()
    print "Recieved Connection from, %s." % str(address)
    while 1:
        provide_task(clientsocket,i)
    clientsocket.close()

def provide_task(s,i):
    print "Sending task."
    task = "r=%d+%d\n"%(i,i) # Must define r and end with 1010011010
    s.send(task)
    try:
        result = s.recv(2048)
        print "Recieved result. Result is, " , result
    except:
        print "Connection Closed by client."

main()