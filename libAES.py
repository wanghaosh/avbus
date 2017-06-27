#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
avbus555 web api service
"""

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

def encrypt(sData, sKey, sIV=b'0000000000000000'):
#{
	mode = AES.MODE_CBC
	encryptor = AES.new(sKey, mode, sIV)
	nAddLen = 16 - (len(sData) % 16)
	sData = sData + ('\0' * nAddLen)
	sRet = encryptor.encrypt(sData)
	return b2a_hex(sRet)
#}

def decrypt(sData, sKey, sIV = b'0000000000000000'):
#{
	sData = a2b_hex(sData)
	print sData
	mode = AES.MODE_CBC
	decryptor = AES.new(sKey, mode, sIV)
	sRet = decryptor.decrypt(sData)
	return sRet.rstrip('\0')
#}

#-------------------------------------------------------#
if __name__ == '__main__':
#{
	print encrypt('1c6b7cda856b9245ec0b899324d2c016b770bc100efcd1e360dbc686c6e8d4c346b6d4750ae58cb6588a39dd4dcc4467d457f6fd0b3664b8108a49b285f47592a4d5e02890569eb38a40cb62be9712758ca31a34a68d112e4fb3ac91d99237bf',
			'avbus555fhzidian')
#」
