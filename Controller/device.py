from time import sleep
import threading


class Device():
    
    def __init__(self) -> None:
        self.watt = 0 
        self.time = 0

    def consuming(self):
        print("Casa consumindo energia")
        while(True):
            sleep(1)
            self.time += 1

    def get_consumption(self):
        return self.watt * (self.time/60)
    

    def set_wat(self, new_watt):
        self.watt = new_watt


device = Device()
threading.Thread(target=device.consuming).start()

'''
while(True):
    sleep(5)
    print("Tempo de consumo: {}".format(device.time))
'''