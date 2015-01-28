import socket
import threading

PORT = 2603
LIM = 2048 # 2 KB

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', PORT))

def main():
    print ""
    print "Started Running srever on this machine."
    print "Waiting for connections"
    print "Run \"ipconfig\" in cmd to get server IP."
    print "Type Ctrl-Break to end server."
    print ""
    serversocket.listen(5)
    jobs = []
    for i in range(4):
        p = threading.Thread(target=worker,args=(i,))
        jobs.append(p)
        p.start()

def worker(i):
    (clientsocket, address) = serversocket.accept()
    print "Recieved Connection from, %s." % str(address)
    e = False
    while not e:
        e = provide_task(clientsocket,i)
    clientsocket.close()

def provide_task(s,i):
    print "Sending task."
    task = "%d"%(i)
    try:
        s.send(task)
        result = s.recv(LIM)
        print "Recieved result. Result is, " , result
        return 0
    except:
        print "Connection Closed by client. <>"
        return 1

main()