#Needed for generating randomized lost packets
import random
import socket

#Create UDP diagram
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Assign IP address and port to socket
server_socket.bind(('', 12000))

while True:
    #generate random number in the range of 0 to 10
    rand = random.randint(0,10)
    #Receive the client packet along with the address it is coming from
    message, address = server_socket.recvfrom(1024)
    #Capitilize message from client
    message = message.upper()
    #If rand is less than 4 we consider the packet lost and do nothing
    if rand >=4:
        continue
    server_socket.sendto(message, address)
