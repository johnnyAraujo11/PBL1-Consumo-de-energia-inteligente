from time import sleep
import threading
import socket


class MeasurerUDP():

    def __init__(self, host='localhost', port=5000) -> None:
        self.port = port
        self.host = host
        self.UDP_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.buffer_size = 1024

    def send_message(self):
        msg_bytes = str.encode('{id":"001","pontecy":"500", "date": "08/03/2023", "time_on":"500"')
        self.UDP_client.sendto(msg_bytes, (self.host, self.port))


    def time_to_send_message(self):
        while(True):
            sleep(5)
            self.send_message()


    def start(self):
        threading.Thread(target=self.time_to_send_message, daemon=True).start()
        t = 0
        #somente para executar a thread em segundo plano
        while(True):
            watt = int(input("O consumo atual é x digite a potência para alterar o consumo: "))
            sleep(1)
            t += 1
            print(t)


measurer = MeasurerUDP()
measurer.start()

 
