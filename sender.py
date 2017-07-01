from Transmission import Transmission, Data
from Transmitter import Transmitter
from Converter import Converter
import DataTypes
import sys

dtype = getattr(DataTypes, sys.argv[1])
args = sys.argv[2:]

transmitter = Transmitter()

converter = Converter()
message = dtype()
message.setup(args)
transmission = Transmission(converter.strtobin('{"type": "' + message.__class__.__name__ + '", "data": "' + message.serialize() + '"}'))


print('starting to transmit')
transmitter.transmit(transmission)
print('')