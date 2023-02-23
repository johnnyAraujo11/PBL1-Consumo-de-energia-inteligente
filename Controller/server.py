import socket 
import sys
import os

dir_abs = os.path.dirname(os.path.realpath(__file__))
new = dir_abs[:-10]
new = new + "Model"
sys.path.insert(0, new)
from routers import *

class Server:
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.data_payload = 2048 


    def connect(self):
        try:
            self.con_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.con_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_address = (self.host, self.port)
            print ("Starting up echo server on:%s port:%s" % self.server_address)
            self.con_socket.bind(self.server_address)
            self.con_socket.listen()
        except:
            print("Fail when starting the server")


    def receive_msg(self):
        try:
            while True:
                print ("Waiting to receive message from client")
                client, address = self.con_socket.accept()
                data = client.recv(self.data_payload)

                self.request_type(data.decode('utf-8'))

                resp = "HTTP/1.0 200 OK\n\nHello World"
                client.sendall(resp.encode())
                client.close()
        except:
            print("Fail when receive message")

    def request_type(self, msg):
        if 'GET' in msg:
            print(all_requests_get(self.split_msg(msg)))
            

    def split_msg(self,msg):
        client_router = msg.split()
        return client_router[1]
        


start_server = Server("localhost", 8080)
start_server.connect()
start_server.receive_msg()
