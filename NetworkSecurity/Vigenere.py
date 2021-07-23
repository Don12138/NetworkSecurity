# -*- coding:utf-8 -*-
import base64

class vigenere:
    def __init__(self, data, key):
        self.__key = key
        self.__data = data

    def encrypt(self):
        new_data = []
        new_key = []
        for i in range(len(self.__data)):
            new_data.append(self.__data[i])
        for i in range(len(self.__key)):
            new_key.append(self.__key[i])

        # 计算new_data对应的数字
        for i in range(len(new_data)):
            new_data[i] = (new_data[i] + new_key[i % len(new_key)]) % 128
        # 将数字转为字符
        for i in range(len(new_data)):
            new_data[i] = chr(new_data[i])

        # 字符进行base64加密
        string = ""
        for i in range(len(new_data)):
            string += new_data[i]
        string = base64.b64encode(string.encode('utf-8'))
        return string

    def decrypt(self):
        self.__data = base64.b64decode(self.__data)
        new_data = []
        new_key = []

        for i in range(len(self.__data)):
            new_data.append(self.__data[i])
        for i in range(len(self.__key)):
            new_key.append(self.__key[i])

        for i in range(len(new_data)):
            new_data[i] = (new_data[i] - new_key[i % len(new_key)]) % 128
        for i in range(len(new_data)):
            new_data[i] = chr(new_data[i])

        string = ""
        for i in new_data:
            string += i
        return string
