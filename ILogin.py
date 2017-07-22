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

def _ILogin(sToken, log):
	"""
	interface: get one program's number(fanhao)
	param:
		token: user token, {"uid":"xxxx", "dt": "yyyymmddHHMMSS", "debug":true, }
		id: program's id(database primary key)
	"""
#{
	if sToken is None:
		return '{"result": "-ERR", "msg": "not fount parameter [token]", "errcode": "E001"}'

	sToken = decrypt(sToken, 'avbus555fhzidian')

	jsToken = None
	# try:
	# #{
	# print '[' + sToken + ']'
	sToken = sToken.replace(' ', '')
	sToken = sToken.split('}')[0] + '}'
	jsToken = json.loads(sToken)
	# #}
	# except:
	# #{
	# 	return '{"result": "-ERR", "msg": "illegl token 1", "errcode": "E002"}'
	# #}

	if jsToken.has_key('uid') is False:
		return '{"result": "-ERR", "msg": "illegl token 2", "errcode": "E003"}'
	if jsToken.has_key('dt') is False:
		return '{"result": "-ERR", "msg": "illegl token 3", "errcode": "E004"}'

	# user = CUser(jsToken['uid'])
	# if user.UsePoint(1) is False:
	# 	return '{"result": "-ERR", "msg": "积分不足，请明天再来（凌晨1点积分自动恢复）.", "errcode": "E005"}'

	# bDebug = False
	# if jsToken.has_key('debug') is True:
	# 	bDebug = jsToken['debug']

	if jsToken.has_key('v') is False:
		return '{"result": "-ERR", "msg": "illegl token 3", "errcode": "E007"}'

	log.Info('login|' + json.dumps(jsToken, ensure_ascii=False))

	nVer = int(jsToken['v'])
	jsRet = {
		'lastVerCode': 4,
		'lastVerURI': 'http://update.avbus.club/t',
		'forceUpdate': 0
	}

	return json.dumps(jsRet, ensure_ascii=False)
#}

#-------------------------------------------------------#
if __name__ == '__main__':
#{
	sToken = '11bad81b6772098ea2552f5a450eda063975202004e70634c32398b3971e37eeff2168373ec7aad411daa2cf9aa1a1c42daaaafab672f1024436728b018560fbd3e7b1b89f956c89c4bbbadd7aeed2ad3e5433c345ae61551494ac6ae73f9724'
	# _IGetNo(sToken, '28072', None)
#}