class Data:
    pass

class Transmission:
    def __init__(self, binary):
        self.__data = Data
        self.__data.binary = binary

    def getrawbinary(self):
        return self.__data.binary

    def getbinary(self):
        return self.getrawbinary() + self.END

    def setbinary(self, value):
        self.__data.binary = value

    def addbinary(self, bool):
        self.setbinary(self.getrawbinary() + str(bool))

    def arecharscomplete(self):
        return len(self.getrawbinary()) % 8 == 0

    def iscomplete(self):
        return self.arecharscomplete() and self.getrawbinary().endswith(self.END)

    END = '00000100'