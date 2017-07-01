from Transmission import Transmission

class Converter:

    def strtobin(self, str):
        ret = ''
        for char in str:
            binary = bin(ord(char))[2:]
            while len(binary) < 8:
                binary = '0' + binary
            ret = ret + binary
        return ret

    def bintostr(self, binary):
        binary = str(binary)
        ret = ""
        i = 0
        while binary[-8:] == Transmission.END:
            binary = binary[:-8]
            
        while i+8 <= len(binary):
            ret = ret + chr(int(binary[i:i+8], 2))
            i = i+8
        return ret