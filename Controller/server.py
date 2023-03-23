import socket 
import threading
import http_req 
import api
import msg_measurer
 

class Server:
    
    def __init__(self, host='172.16.103.207', port_TCP=52525, port_UDP=52526):
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
            threading.Thread(target=self.client_connect_TCP).start()
            threading.Thread(target=self.client_connect_UDP).start()
        except:
            print("Fail when starting the server")


    '''
    Função que aguarda os medidores enviarem dados e salva em um arquivo json.
    '''
    def client_connect_UDP(self):
        while(True):
            print("waiting message from measurer")
            bytesAddressPair = self.UDPServerSocket.recvfrom(self.data_payload)
            message = bytesAddressPair[0]
            clientMsg = "Message from Client:{}".format(message)
            print(clientMsg)
            msg_measurer.save_json(message.decode())
            
            
    '''
    Função que aguarda a conexão de clientes.
    '''
    def client_connect_TCP(self):
            while True:
                print ("Waiting to receive message from client")
                client, address = self.con_socket.accept()
                client_thread = threading.Thread(target=self.handle_client_TCP, args=(client, address), daemon=True)
                client_thread.start()
                
                
    '''
    Recebe clientes e suas respectivas mensagens http
    '''
    def handle_client_TCP(self, client, addr):
        print("New connection by {}".format(addr))
        data = client.recv(1024)
        if data:
            _api = api.API(data.decode())
            response = _api.response()
            client.send(response.encode('utf-8'))
            client.close()  
        print("Close connection")


