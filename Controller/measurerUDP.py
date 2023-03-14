from time import sleep
import threading
import socket
import device
import json
from datetime import time, datetime



class MeasurerUDP():

    def __init__(self, num_measurer, device, host='localhost', port=5000) -> None:
        self.port = port
        self.host = host
        self.UDP_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.buffer_size = 1024
        self.num_measurer = num_measurer
        self.device = device
        self.time = 0.0



    def send_message(self):
        _date = datetime.now()

        msg = {"id":self.num_measurer, "consumption":  self.consumption(), "date_hour": _date.strftime("%d/%m/%Y %H:%M")}
        json_msg = json.dumps(msg)
        
        msg_bytes = str.encode(json_msg)
        self.UDP_client.sendto(msg_bytes, (self.host, self.port))


    def time_to_send_message(self):
    
        while(True):
            sleep(1)
            self.time += 1
            if(self.time == 5):
                self.send_message()
                self.time = 0


    def start(self):
        threading.Thread(target=self.time_to_send_message, daemon=True).start()
        #somente para executar a thread em segundo plano
        while(True):
            device.watt = float(input("O consumo atual é x digite a potência para alterar o consumo: "))
            
    
    def consumption(self):
        return round((self.time / 3600) * device.watt, 2)



device = device.Device()

measurer = MeasurerUDP("001", device)
measurer.start()

 
