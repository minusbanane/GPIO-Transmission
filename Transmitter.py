import RPi.GPIO as gpio
import sys

class Transmitter:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(17, gpio.OUT)
        gpio.setup(27, gpio.IN)
        self.is_send = gpio.input(27)
        gpio.setup(27, gpio.OUT)
        gpio.setup(22, gpio.IN)

        self.has_read = gpio.input(22)

    def transmit(self, transmission):
        i = 0
        length = len(transmission.getbinary())
        for bool in str(transmission.getbinary()):
            i = i + 1
            gpio.output(17, int(bool))
            self.is_send = not self.is_send
            gpio.output(27, self.is_send)
            while self.has_read == gpio.input(22):
                pass
            self.has_read = gpio.input(22)
            sys.stdout.write('\r')
            sys.stdout.write(str(i) + ' of ' + str(length) + ' bits (' + str(round(i / length * 100, 1)) + '%)')
        print('')