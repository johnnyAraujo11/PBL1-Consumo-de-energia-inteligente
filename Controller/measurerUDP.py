from time import sleep
import threading
import socket
import device

class MeasurerUDP():

    def __init__(self, host='localhost', port=5000) -> None:
        self.port = port
        self.host = host
        self.UDP_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.buffer_size = 1024

    def send_message(self, device):
        msg_bytes = str.encode('{"id":"001","pontecy":{}, "date": "08/03/2023", "time_on":"500", "hour":"10:00"}'.format(device.get_consumption()))
        self.UDP_client.sendto(msg_bytes, (self.host, self.port))


    def time_to_send_message(self, device):
        while(True):
            sleep(5)
            self.send_message(device)


    def start(self, device):
        threading.Thread(target=self.time_to_send_message,args=(device,), daemon=True).start()
        t = 0
        #somente para executar a thread em segundo plano
        while(True):
            watt = int(input("O consumo atual é x digite a potência para alterar o consumo: "))
            sleep(1)
            t += 1
            print(t)

device = device.Device()
device.start()

measurer = MeasurerUDP()
measurer.start(device)

 
