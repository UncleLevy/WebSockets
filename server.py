#!/user/bin/python3
#python file for web sockets

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket object

host = socket.gethostname() #get local machine name
port = 444 #reserve a port for your service

serversocket.bind((host, port)) #bind to the port

serversocket.listen(3) #queue up to 3 requests

while True:
    clientsocket, address = serversocket.accept() #establish a connection

    print("Received connection from %s " % str(address)) #print the address of the client

    message = 'Hello! Thank you for connecting to the server' + "\r\n."
    clientsocket.send(message.encode('ascii')) #send a thank you message to the client

    clientsocket.close() #close the connection 