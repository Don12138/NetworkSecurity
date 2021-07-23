import time

import websockets
import asyncio
import Vigenere
import people
import signatureOfRSA


class Client:
    def __init__(self, name):
        self.person = people.People(name)

    async def listen(self, uri):
        async with websockets.connect(uri) as websocket:
            while True:
                message = input("是否要发送文件(y/n):      ")
                if message != "":
                    if message == "y":
                        message = input("请输入文件地址:                   ")
                        with open(message, 'rb') as f:
                            data = f.read()
                        string = self.generate_string(data,False)
                    else:
                        message = input("请输入你要发送的信息:                    ")
                        string = self.generate_string(bytes(message,encoding='utf-8'),True)
                    await websocket.send(string)
                    recv_text = await websocket.recv()
                    print("消息发送成功:                  "+recv_text)
                    continue
                recv_text = await websocket.recv()
                self.handle_string(recv_text)
                time.sleep(1)

    def generate_string(self, data,ismessage):
        vigenere = Vigenere.vigenere(data, self.person.getVigenere())
        signature = signatureOfRSA.SignatureOfRSA(self.person, data)

        secret_message = str(vigenere.encrypt(), encoding="utf-8")  # 获取Alice秘文
        ensignature_signature = str(signature.ensignature(), encoding="utf-8")  # 获取Alice数字签名
        public_key = str(self.person.getPublic(), encoding="utf-8")  # 获取Alice公钥

        string = ''
        string = self.generate_unit(string,'1' if ismessage else '2')
        string = self.generate_unit(string, secret_message)
        string = self.generate_unit(string, ensignature_signature)
        string = self.generate_unit(string, public_key)

        return string

    def generate_unit(self, string, data):
        string += str(len(data)).zfill(10)
        string += data
        return string

    def handle_string(self,string):
        length = int(string[0:10])
        is_message = string[10:length+10]
        string = string[length+10:]
        length = int(string[0:10])
        secret_message = string[10:length+10]
        string = string[length+10:]
        length = int(string[0:10])
        ensignature_signature = string[10:length + 10]
        string = string[length + 10:]
        public_key = string[10:]

        if is_message == '1':
            vigenere = Vigenere.vigenere(bytes(secret_message,encoding="utf-8"), self.person.getVigenere())
            true_message = vigenere.decrypt()
            print("收到消息:                    "+true_message)

            signature = signatureOfRSA.SignatureOfRSA(self.person, bytes(true_message,encoding="utf-8"))
            print("数字签名认证:                  "+str(signature.verifySignture(public_key,bytes(ensignature_signature,encoding="utf-8"))))

        elif is_message == '2':
            vigenere = Vigenere.vigenere(bytes(secret_message, encoding="utf-8"), self.person.getVigenere())
            true_message = vigenere.decrypt()
            with open(self.person.getName()+"_Storage/"+self.person.getName()+'-File.txt', 'wb') as f:
                f.write(bytes(true_message,encoding='utf-8'))
            print("成功接受文件")
            signature = signatureOfRSA.SignatureOfRSA(self.person, bytes(true_message, encoding="utf-8"))
            print("数字签名认证:                  " + str(
                signature.verifySignture(public_key, bytes(ensignature_signature, encoding="utf-8"))))
