import time
import json
from Converter import Converter
from PIL import Image

class DataType:
    pass

class Message(DataType):
    def __init__(self):
        self.__send = time.time()
        self.converter = Converter()

    def setup(self, args = None):
        if args is None:
            self.__author = input('Autor: ')
            self.__text = input('Text: ')
        else:
            self.__author = args[0]
            self.__text = args[1]

    def serialize(self):
        return self.converter.strtobin(json.dumps({
            'author': self.__author,
            'text': self.__text,
            'send': self.__send
        }))

    def deserialize(self, serialized):
        desered = json.loads(self.converter.bintostr(serialized))
        self.__author = desered['author']
        self.__text = desered['text']
        self.__send = desered['send']

    def display(self):
        print(self.__author + ': ' + self.__text + ' (' + str(round(time.time() - self.__send,3)) + ' ticks)')


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

class ImageASCII(DataType):
    def __init__(self):
        self.converter = Converter()

    def setup(self, args = None):
        if args is None:
            self.__file = input('Bildnamen eingeben: ')
        else: 
            self.__file = args[0]

    def serialize(self):
        return self.converter.strtobin(json.dumps(self.convert_image_to_ascii(Image.open(self.__file))))

    def deserialize(self, serialized):
        self.__art = json.loads(self.converter.bintostr(serialized))

    def display(self):
        for line in self.__art:
            print(line)

    def scale_image(self, image, new_width=100):
        """Resizes an image preserving the aspect ratio.
        """
        (original_width, original_height) = image.size
        aspect_ratio = original_height/float(original_width)
        new_height = int(aspect_ratio * new_width)

        new_image = image.resize((new_width, new_height))
        return new_image

    def convert_to_grayscale(self, image):
        return image.convert('L')

    def map_pixels_to_ascii_chars(self, image, range_width=25):
        """Maps each pixel to an ascii char based on the range
        in which it lies.

        0-255 is divided into 11 ranges of 25 pixels each.
        """

        pixels_in_image = list(image.getdata())
        pixels_to_chars = [self.ASCII_CHARS[int(pixel_value/range_width)] for pixel_value in
                pixels_in_image]

        return "".join(pixels_to_chars)

    def convert_image_to_ascii(self, image, new_width=100):
        image = self.scale_image(image)
        image = self.convert_to_grayscale(image)

        pixels_to_chars = self.map_pixels_to_ascii_chars(image)
        len_pixels_to_chars = len(pixels_to_chars)

        image_ascii = [pixels_to_chars[index: index + new_width] for index in
                range(0, len_pixels_to_chars, new_width)]

        return image_ascii

    ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']