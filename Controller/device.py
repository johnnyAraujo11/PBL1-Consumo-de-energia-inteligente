from time import sleep
import threading


class Device():

    def __init__(self):
<<<<<<< HEAD
        self.watt = 1000.0 
=======
        self.watt = 1000 
        self.time = 0

    def consuming(self):
        print("Casa consumindo energia\n")
        while(True):
            sleep(1)
            self.time += 1
>>>>>>> 3f6de7f99478b251d0c9eb06ead1c38cb13bedfd

    def get_watt(self):
        return self.watt

    def set_watt(self, new_watt):
        self.watt = new_watt


<<<<<<< HEAD
=======
    def start(self):
        threading.Thread(target=self.consuming).start()

#device = Device()
#threading.Thread(target=device.consuming).start()

'''
while(True):
    sleep(5)
    print("Tempo de consumo: {}".format(device.time))
'''
>>>>>>> 3f6de7f99478b251d0c9eb06ead1c38cb13bedfd
