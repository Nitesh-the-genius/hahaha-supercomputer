import time # remove this later TODO
import socket

PORT = 2603
server = raw_input("Enter Server address: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server,PORT))

def main():
    while 1:
        a = s.recv(2048)
        print "Recieved task. Processing task."
        r = process_task(a)
        print "Result is, ", r
        s.send(str(r))
        print "Asking for next task."

def process_task(t):
    exec t # Should define r
    time.sleep(1)
    return r

main()