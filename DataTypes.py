import time
import json
from Converter import Converter

class DataType:
    pass

class Message(DataType):
    def __init__(self):
        self.__send = time.time()

    def setup(self, args = None):
        self.__author = input('Autor: ')
        self.__text = input('Text: ')

    def serialize(self):
        return json.dumps({
            'author': self.__author,
            'text': self.__text,
            'send': self.__send
        })

    def deserialize(self, serialized):
        desered = serialized
        self.__author = desered['author']
        self.__text = desered['text']
        self.__send = desered['send']

    def display(self):
        print(self.__author + ': ' + self.__text)


class TextFile(DataType):
    def __init__(self):
        self.converter = Converter()

    def setup(self, args = None):
        if args is None:
            self.__file = input('Dateinamen eingeben: ')
        else: 
            self.__file = args[0]

    def serialize(self):
        return self.converter.strtobin(str(open(self.__file, 'r').read()))

    def deserialize(self, serialized):
        self.__filecontent = self.converter.bintostr(str(serialized))

    def display(self):
        print('Datei empfangen!')
        self.__file = input('Zielverzeichnis eingeben: ')
        open(str(self.__file), 'w').write(str(self.__filecontent))