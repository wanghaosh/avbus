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
	print decrypt('11bad81b6772098ea2552f5a450eda063975202004e70634c32398b3971e37eeff2168373ec7aad411daa2cf9aa1a1c42daaaafab672f1024436728b018560fbd3e7b1b89f956c89c4bbbadd7aeed2ad3e5433c345ae61551494ac6ae73f9724',
			'avbus555fhzidian')
#」
