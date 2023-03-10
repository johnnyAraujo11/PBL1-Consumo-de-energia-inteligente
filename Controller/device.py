from time import sleep
import threading


class Device():

    def __init__(self):
        self.watt = 1000 
        self.time = 0

    def consuming(self):
        print("Casa consumindo energia\n")
        while(True):
            sleep(1)
            self.time += 1

    def get_watt(self):
        return self.watt
    

    def set_watt(self, new_watt):
        self.watt = new_watt


    def start(self):
        threading.Thread(target=self.consuming).start()

#device = Device()
#threading.Thread(target=device.consuming).start()

'''
while(True):
    sleep(5)
    print("Tempo de consumo: {}".format(device.time))
'''