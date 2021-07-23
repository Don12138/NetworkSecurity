class People:
    def __init__(self, name):
        self.__name = name

    def getPrivate(self):
        with open(self.__name + '_Storage/' + self.__name + '-private.txt', 'rb') as f:
            key = f.read()
        return key

    def getPublic(self):
        with open(self.__name + '_Storage/' + self.__name + '-public.txt', 'rb') as f:
            key = f.read()
        return key

    def getVigenere(self):
        with open(self.__name + '_Storage/' + self.__name + '-VigenereKey.txt', 'rb') as f:
            key = f.read()
        return key

    def getName(self):
        return self.__name