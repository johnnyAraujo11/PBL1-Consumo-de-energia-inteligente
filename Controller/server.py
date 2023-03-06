import socket 
import sys
import os
import threading
import http_req 
import API

'''
dir_abs = os.path.dirname(os.path.realpath(__file__))
new = dir_abs[:-10]
new = new + "Model"

sys.path.insert(0, new)
from API import *
'''

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
            #self.server_address = ('172.17.0.1', self.port)
            print ("Starting up echo server on:%s port:%s" % self.server_address)
            self.con_socket.bind(self.server_address)
            self.con_socket.listen()
        except:
            print("Fail when starting the server")


    def client_connect(self):
            while True:
                print ("Waiting to receive message from client")
                client, address = self.con_socket.accept()
                #client_thread = threading.Thread(target=self.handle_client, args=(client, address), daemon=True)
                #client_thread.start()
                self.handle_client(client, address)
         


    def handle_client(self, client, addr):
        print("New connection by {}".format(addr))
        data = client.recv(1024)
        if data:
            #http_req.http_request(data.decode("utf-8"))
            resp = b"HTTP/1.0 200 OK\n\nHello World"
            str_http = http_req.Http_request(data.decode())
            
            response = API.all_requests_get("/consumption") if "GET" == str_http.method else  API.all_request_post("/consumption")

            client.send(response.encode('utf-8'))
            client.close()  
            
        print("Close connection")



    def request_type(self, msg):
        if 'GET' in msg:
            return API.all_requests_get(self.split_msg(msg)[0])


start_server = Server("localhost", 8080)
start_server.connect()
start_server.client_connect()
