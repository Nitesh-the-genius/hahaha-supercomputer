import socket

PORT = 2603
server = raw_input("Enter Server address: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server,PORT))
s.send("Hello")
