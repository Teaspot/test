# -*- coding: utf-8 -*-

from pyDes import *
import base64

# Des CBC
# 自定IV向量
Des_IV = b"\xef\xab\x56\x78\x90\x34\xcd\x12"

def DesEncrypt(str,key):
    # str 明文password
    # key uid
    Des_Key = (key+"0000")[0:8]
    k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
    EncryptStr = k.encrypt(str)
    return base64.b64encode(EncryptStr) #转base64编码返回

def DesDecrypt(str,key):
    # str 密文password
    # key uid
    Des_Key = (key+"0000")[0:8]
    EncryptStr = base64.b64decode(str)
    print(EncryptStr)
    k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
    DecryptStr = k.decrypt(EncryptStr)
    return DecryptStr