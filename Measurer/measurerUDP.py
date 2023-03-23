from time import sleep
import threading
import socket
import device
import json
from datetime import time, datetime
import random as rd


class MeasurerUDP():

    def __init__(self, num_measurer, device, host='172.16.103.207', port=52526) -> None:
        self.port = port
        self.host = host
        self.UDP_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.buffer_size = 1024
        self.num_measurer = num_measurer
        self.device = device
        self.time = 5

    '''
    Montagem da mensagem para ser enviada
    '''
    def send_message(self):
        _date = datetime.now()

        msg = {"id":self.num_measurer, "consumption":  device.get_watt(), "date_hour": _date.strftime("%d/%m/%Y %H:%M")}
        json_msg = json.dumps(msg)
        
        msg_bytes = str.encode(json_msg)
        self.UDP_client.sendto(msg_bytes, (self.host, self.port))

    '''
    Envia a mensagem a cada 5 segundos
    '''
    def time_to_send_message(self):
        while(True):
            sleep(self.time)
            #print("sending: {}".format(device.get_watt()))
            self.send_message()


    def start(self):
        threading.Thread(target=self.time_to_send_message).start()
        #threading.Thread(target=self.generate_watt).start()
        print("Medidor: {}".format(self.num_measurer))
        while(True):
            device.watt = float(input("Digite a potência em watt para alterar o consumo, aumentando ou diminuindo: "))
            

    '''
    Gera uma potência aleatória 
    '''
    def generate_watt(self):
        while(True):
            device.set_watt(rd.randint(0,2000))
        

device = device.Device()
measurer = MeasurerUDP("7024", device)
measurer.start()

 
