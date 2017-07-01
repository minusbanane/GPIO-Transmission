import RPi.GPIO as gpio
from Transmission import Transmission
from Converter import Converter
import sys

class Receiver:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(18, gpio.IN)
        gpio.setup(23, gpio.IN)
        gpio.setup(24, gpio.IN)
        self.is_read = gpio.input(24)
        gpio.setup(24, gpio.OUT)

        
        self.has_send = gpio.input(23)

        self.transmission = Transmission('')
        self.converter = Converter()

    def watch(self):
        self.transmission.setbinary('')
        while not self.transmission.iscomplete():
            if(self.has_send is not gpio.input(23)):
                self.transmission.addbinary(str(gpio.input(18)))
                self.has_send = gpio.input(23)
                self.is_read = not self.is_read
                gpio.output(24, self.is_read)
                sys.stdout.write('\r')
                sys.stdout.write(str(len(self.transmission.getrawbinary())) + ' bits Received')
        sys.stdout.write('\r')
        sys.stdout.write('                                                                    ')
        return self.transmission