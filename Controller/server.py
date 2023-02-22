import socket 

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
            self.con_socket.listen(2)
        except:
            print("Fail when starting the server")


    def receive_msg(self):
        try:
            while True:
                print ("Waiting to receive message from client")
                client, address = self.con_socket.accept()
                data = client.recv(self.data_payload)
                if data:
                    print("dados: %s" % data)
                    resp = "HTTP/1.0 200 OK\n\nHello World"
                    client.sendall(resp.encode())
                    client.close()
        except:
            print("Fail when receive message")


start_server = Server("localhost", 8080)
start_server.connect()
start_server.receive_msg()