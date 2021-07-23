# -*- coding:utf-8 -*-
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA1
import base64


class SignatureOfRSA:
    def __init__(self, usr, data):
        self.user = usr
        self.__data = data

    # 使用私钥对内容进行签名
    def ensignature(self):
        key = self.user.getPrivate()
        rsaKey = RSA.importKey(key)  # 签名使用私钥
        signer = PKCS1_v1_5.new(rsaKey)
        h = SHA1.new(self.__data)
        sign = signer.sign(h)
        return base64.b64encode(sign)

    # 验证签名
    def verifySignture(self, public_key,signature):
        rsaKey = RSA.importKey(public_key)  # 验证签名使用公钥
        signer = PKCS1_v1_5.new(rsaKey)
        h = SHA1.new(self.__data)
        return signer.verify(h, base64.b64decode(signature))
