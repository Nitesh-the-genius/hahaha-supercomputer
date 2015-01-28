import socket
import tasks

PORT = 2603
LIM = 2048

server = raw_input("Enter Server address: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server,PORT))

def main():
    while 1:
        a = s.recv(LIM)
        print "Recieved task. Processing task."
        r = process_task(a)
        print "Result is, ", r
        s.send(str(r))
        print "Asking for next task."

def process_task(t):
    t = int(t)
    board = [[0,0,0],[0,0,0],[0,0,0]]
    board[t/3][t%3] = 1
    r = tasks.minimax(board)
    return r

main()