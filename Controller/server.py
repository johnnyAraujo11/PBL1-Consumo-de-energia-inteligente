import socket 
import sys
import os
import threading
import http_req 
import api
import msg_measurer


'''
dir_abs = os.path.dirname(os.path.realpath(__file__))
new = dir_abs[:-10]
new = new + "Model"

sys.path.insert(0, new)
from API import *
'''

class Server:
    
    def __init__(self, host='localhost', port_TCP=8080, port_UDP=5000):
        self.host = host
        self.port_TCP = port_TCP
        self.port_UDP = port_UDP
        self.data_payload = 2048 
        

    def connect(self):
        try:
            self.con_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.con_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_address = (self.host, self.port_TCP)
            self.con_socket.bind(self.server_address)
            self.con_socket.listen()


            self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            self.UDPServerSocket.bind((self.host, self.port_UDP))
            print ("Starting up echo server TCP on:{} port:{}\nStarting up echo server UDP on:{} port:{}".format(self.host,self.port_TCP, self.host, self.port_UDP))
            # Criando duas threads para executar os tipos de conexões(TCP e UDP)    
            serverTCP = threading.Thread(target=self.client_connect_TCP).start()
            serverUDP = threading.Thread(target=self.client_connect_UDP).start()
        except:
            print("Fail when starting the server")


    def client_connect_UDP(self):
        while(True):
            print("waiting message from measurer")
            bytesAddressPair = self.UDPServerSocket.recvfrom(self.data_payload)
            message = bytesAddressPair[0]
            #address = bytesAddressPair[1]
            clientMsg = "Message from Client:{}".format(message)
            #clientIP  = "Client IP Address:{}".format(address)
            print(clientMsg)
            msg_measurer.save_json(message.decode())
            

    def client_connect_TCP(self):
            while True:
                print ("Waiting to receive message from client")
                client, address = self.con_socket.accept()
                client_thread = threading.Thread(target=self.handle_client_TCP, args=(client, address), daemon=True)
                client_thread.start()
                

    def handle_client_TCP(self, client, addr):
        print("New connection by {}".format(addr))
        data = client.recv(1024)
        #print(data.decode())
        if data:
            _api = api.API(data.decode())
            response = _api.response()
            client.send(response.encode('utf-8'))
            client.close()  
            
        print("Close connection")

    
'''start_server = Server()
start_server.connect()'''

