from time import sleep
import threading


class Device():

    def __init__(self):
        self.watt = 1000.0 

    def get_watt(self):
        return self.watt

    def set_watt(self, new_watt):
        self.watt = new_watt


