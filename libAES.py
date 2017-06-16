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
	mode = AES.MODE_CBC
	decryptor = AES.new(sKey, mode, sIV)
	sRet = decryptor.decrypt(sData)
	return sRet.rstrip('\0')
#}
