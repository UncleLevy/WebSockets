#!/user/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket object

host = socket.gethostname() #get local machine name

port = 444 #reserve a port for service

clientsocket.connect((host, port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii')) #print the message