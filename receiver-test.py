from Transmission import Transmission, Data
from Receiver import Receiver
from Converter import Converter
import json
import DataTypes

receiver = Receiver()
converter = Converter()

print('waiting for transmission')

while True:
    transmission = json.loads(converter.bintostr(receiver.watch().getrawbinary()))
    req_class = getattr(DataTypes, transmission['type'])

    data_object = req_class()
    data_object.deserialize(transmission['data'])
    data_object.display()