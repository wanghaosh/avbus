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

def _IGetNo(sToken, sID, log):
	"""
	interface: get one program's number(fanhao)
	param:
		token: user token, {"uid":"xxxx", "dt": "yyyymmddHHMMSS", "debug":true}
		id: program's id(database primary key)
	"""
#{
	if sToken is None:
		return '{"result": "-ERR", "msg": "not fount parameter [token]", "errcode": "E001"}'

	sToken = decrypt(sToken, 'avbus555fhzidian')

	jsToken = None
	# try:
	# #{
	print sToken
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

	user = CUser(jsToken['uid'])
	if user.UsePoint(1) is False:
		return '{"result": "-ERR", "msg": "no enough point.", "errcode": "E005"}'

	bDebug = False
	if jsToken.has_key('debug') is True:
		bDebug = jsToken['debug']

	if sID is None:
		return '{"result": "-ERR", "msg": "not fount parameter [id]", "errcode": "E006"}'

	sMode = 'mem'
	mem = CMemCached()
	sKey = 'api_getno_' + sID
	sKey = sKey.encode('utf-8')
	sRet = mem.Get(sKey)

	# sRet = None
	if sRet == '' or sRet is None:
	#{
		sMode = 'db'
		# conn = mysql.connector.connect(
		# 	user='avline555',
		# 	password='avline555',
		# 	host='avline555.clciqyuahjrn.us-east-2.rds.amazonaws.com',
		# 	database='line555'
		# )
		conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')

		cur = conn.cursor()
		#try:
		#{
		sSql = 'select number from programs where id=' + sID
		cur.execute(sSql)
		res = cur.fetchall()

		aryRecs = []
		for r in res:
		#{
			rec = {
				"no":r[0]
			}
			aryRecs.append(rec)
		#}
		cur.close()
		conn.close()
		jsRet = {
			"result":"+OK",
			"count": len(aryRecs),
			"no": aryRecs
		}
		#}
		#except:
		#{
		#	cur.close()
		#	conn.close()
		#}
#		sRet = '{"result":"+OK", "actorcount":' + len(aryRecs) + ', "actors":' + str(aryRecs) + '}'
		# mem.Set(sKey, sRet, 3600 * 24)
		sRet = json.dumps(jsRet, ensure_ascii=False)
		mem.Set(sKey, sRet, 3600 * 24)
	#}
	log.Info('getno|' + sMode)
	sRetData = sRet
	if bDebug is False:
	#{
		sRetData = encrypt(sRetData, 'avbus555fhzidian')
	#}
	return sRetData
#}
#
# def encrypt(sData, sKey, sIV=b'0000000000000000'):
# #{
# 	mode = AES.MODE_CBC
# 	encryptor = AES.new(sKey, mode, sIV)
# 	nAddLen = 16 - (len(sData) % 16)
# 	sData = sData + ('\0' * nAddLen)
# 	sRet = encryptor.encrypt(sData)
# 	return b2a_hex(sRet)
# #}
#
# def decrypt(sData, sKey, sIV = b'0000000000000000'):
# #{
# 	sData = a2b_hex(sData)
# 	mode = AES.MODE_CBC
# 	decryptor = AES.new(sKey, mode, sIV)
# 	sRet = decryptor.decrypt(sData)
# 	return sRet.rstrip('\0')
# #}
