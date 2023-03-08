import socket

 
msgFromClient       = "Hello UDP Server"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("localhost", 5000)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 
# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)


 
