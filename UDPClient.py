#Nathan LeBlanc
#UDP Socket Demo

import time
import socket

recieved = 0
lost = 0
max_RTT = 0
min_RTT = 10
total_RTT = 0
average_RTT = 0

for pings in range(10):
    #Create UDP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #Wait one second for client timeout
    client.settimeout(1.0)
    #message to send to server in bytes
    message = b'message_test'
    #address that message is coming from
    address = ("127.0.0.1", 12000)
    #calculate the time when the message is sent
    start = time.time()
    #Send data to socket
    client.sendto(message, address)

    try:
        #Recieve the server data
        data, server = client.recvfrom(1024)
        #calculate message recieved time
        end = time.time()
        timeReply = time.strftime("%a %d %b %Y %H:%M:%S")
        #calculate total time
        totTime = end - start
        #add to recieved pings
        recieved += 1
        #get max RTT
        if(totTime > max_RTT):
            max_RTT = totTime
        #get min RTT
        if(totTime < min_RTT):
            min_RTT = totTime
        #get total RTT
        total_RTT += totTime
        #print out data, pings, and total time
        print(f"Reply from 127.0.0.1: PING {pings+1} {timeReply} \nRTT: {totTime}")
    
    #When the exception is raised for a timeout occuring print error    
    except socket.timeout:
        print("Request timed out")
        lost += 1

#percent lost
percent_lost = str(round((lost/(pings+1))*100,2))
#average RTT
average_RTT = (total_RTT/recieved)

#print out ping stats
print(f"\nPackets: Sent = {pings+1}, Recieved = {recieved}, Lost = {lost}({percent_lost}% loss),\n Average RTT: {average_RTT},\n Min: {min_RTT},\n Max: {max_RTT}")
