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
import traceback
from gevent import monkey
# from gevent.pywsgi import WSGIServer
# monkey.patch_all()

import mysql.connector
# from Crypto.Cipher import AES
# from binascii import b2a_hex, a2b_hex
# import zlib
import urllib2
# import urllib

from libMemC import CMemCached
from libLog import CLog

# from libUser import CUser

def getFromMemcached(mem, sKey):
#{
	# mem = CMemCached()
	# sKey = 'api_getactorlist'
	# sKey = sKey.encode('utf-8')
	sRet = mem.Get(sKey)

	if sRet == '' or sRet is None:
		return None
	return sRet
#}

def getFromRDS(aryActorIDs):
#{
	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()
	try:
	# {
		sSql = 'select id, name, alias, program_count from actors where status=1 and ('
		bFirst = True
		for sID in aryActorIDs:
		#{
			if bFirst:
			#{
				bFirst = False
				sSql += 'id=' + sID
			#}
			else:
			#{
				sSql += ' or id=' + sID
			#}
		#}
		sSql += ')'

		cur.execute(sSql)
		res = cur.fetchall()

		aryRecs = []
		for r in res:
		# {
		# 	print r
			rec = {
				"id": r[0],
				"actor": r[1],
				"alias": r[2],
				"pic": "https://s3-ap-southeast-1.amazonaws.com/avbus-data/covers/%d.jpg"%(r[0]),
				"programcount": r[3]
			}
			# print rec
			aryRecs.append(rec)
		# }

		cur.close()
		conn.close()

		jsRet = {
			"result": "+OK",
			"actorcount": len(aryRecs),
			"actors": aryRecs,
			"mode": "db"
		}
		# print jsRet
		sRet = json.dumps(jsRet, ensure_ascii=False)
		return sRet

		# return aryRecs
	# }
	except:
	# {
		info = sys.exc_info()
		print str(info)


		print traceback.format_exc()
		cur.close()
		conn.close()

		return None
	# }
	# sRet = '{"result":"+OK", "actorcount":' + len(aryRecs) + ', "actors":' + str(aryRecs) + '}'

	# print 'size: ' + str(len(sRet))
	# sRet = zlib.compress(sRet)
	# print 'z size: ' + str(len(sRet))
	# mem.Set(sKey, sRet, 3600 * 24)

#}

def _IR_a(aryActorIDs, log):
	"""
	"""
#{
	mem = CMemCached()
	sKey = 'api_r_a'
	sKey = sKey.encode('utf-8')

	sRet = getFromMemcached(mem, sKey)
	sRet = None
	if sRet:
	#{
		jsRet = json.loads(sRet)
		jsRet['mode'] = 'mem'

		# log.Info('getactorlist|mem')
		return json.dumps(jsRet, ensure_ascii=False)
	#}

	sRet = getFromRDS(aryActorIDs)
	if sRet:
	#{
		mem.Set(sKey, sRet, 3600 * 24)

		log.Info('r_a|db')
		return sRet
	#}

	return '{"result": "-ERR", "msg": "Not Found Data."}'
#}

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
