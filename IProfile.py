#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
avbus555 web api service
"""

import json
# import base64
# import datetime
# import time
# import urllib2
# import urllib
import sys

from gevent import monkey
# from gevent.pywsgi import WSGIServer
# monkey.patch_all()

import mysql.connector
# from Crypto.Cipher import AES
# from binascii import b2a_hex, a2b_hex
from libAES import encrypt
from libAES import decrypt
import zlib

from libMemC import CMemCached
from libLog import CLog

from libUser import CUser

def _IProfile(sToken, log):
	"""
	"""
#{
	if sToken is None:
		return '{"result": "-ERR", "msg": "not fount parameter [token]", "errcode": "E001"}'

	sToken = decrypt(sToken, 'avbus555fhzidian')

	log.Info('_IProfile|' + sToken)
	jsToken = None
	try:
	#{
	# print '[' + sToken + ']'
		sToken = sToken.replace(' ', '')
		sToken = sToken.split('}')[0] + '}'
		jsToken = json.loads(sToken)
	#}
	except:
	#{
		return '{"result": "-ERR", "msg": "illegl token 1", "errcode": "E002"}'
	#}

	if jsToken.has_key('uid') is False:
		return '{"result": "-ERR", "msg": "illegl token 2", "errcode": "E003"}'
	if jsToken.has_key('dt') is False:
		return '{"result": "-ERR", "msg": "illegl token 3", "errcode": "E004"}'

	user = CUser(jsToken['uid'])
	nPoint = user.GetPoint()
	# print nPoint

	# jsRet = {
	# 	"result":"+OK",
	# 	"point": nPoint
	# }
	# print jsRet
	# return json.dumps(jsRet, ensure_ascii=False)
	sRet = '{"result": "+OK", "point": %d}'%(nPoint)
	return sRet

	#}
	# log.Info('getno|' + sMode)
	# sRetData = sRet
	# if bDebug is False:
	# #{
	# 	sRetData = encrypt(sRetData, 'avbus555fhzidian')
	# #}
	# return sRetData
#}

#-------------------------------------------------------#
if __name__ == '__main__':
#{
	sToken = '11bad81b6772098ea2552f5a450eda063975202004e70634c32398b3971e37eeff2168373ec7aad411daa2cf9aa1a1c42daaaafab672f1024436728b018560fbd3e7b1b89f956c89c4bbbadd7aeed2ad3e5433c345ae61551494ac6ae73f9724'
	_IGetNo(sToken, '28072', None)
#}