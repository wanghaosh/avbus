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

def getFromRDS(nPageIndex, nPageSize):
#{
	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()
	try:
	# {
	#  	sSql = 'select actor_id, actor, count(*) from programs where online=1 group by actor limit %d, %d'%(nPageIndex * nPageSize, nPageSize)
		sSql = 'select id, name, alias, program_count from actors where status=1 and program_count>0 order by id desc limit %d,%d'%(nPageIndex * nPageSize, nPageSize)
		# print sSql
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

def HttpGet(sUri):
# {
	try:
	# {
		resp = urllib2.urlopen(sUri)

		if resp.getcode() != 200:
		# {
			print resp.getcode()
			return None
		# }
		return resp.read()
	# }
	except:
	# {
		info = sys.exc_info()
		print info
		return None
	# }
# }

def getFromS3():
#{
	return HttpGet('https://s3-ap-southeast-1.amazonaws.com/avbus-data/actorlist.json')
#}

def _IGetActorList(nPageIndex, nPageSize, log):
	"""
	interface: get actor list(full)
	"""
#{
	log.Info('_IGetActorList|%d|%d'%(nPageIndex, nPageSize))

	mem = CMemCached()
	sKey = 'api_getactorlist_%d_%d'%(nPageIndex, nPageSize)
	sKey = sKey.encode('utf-8')

	sRet = getFromMemcached(mem, sKey)
	sRet = None
	if sRet:
	#{
		jsRet = json.loads(sRet)
		jsRet['mode'] = 'mem'

		log.Info('getactorlist|mem')
		return json.dumps(jsRet, ensure_ascii=False)
	#}

	# sRet = getFromS3()
	# if sRet:
	# #{
	# 	mem.Set(sKey, sRet, 3600 * 24)
    #
	# 	jsRet = json.loads(sRet)
	# 	jsRet['mode'] = 's3'
	# 	log.Info('getactorlist|s3')
    #
	# 	return json.dumps(jsRet, ensure_ascii=False)
	# #}

	sRet = getFromRDS(nPageIndex, nPageSize)
	if sRet:
	#{
		mem.Set(sKey, sRet, 3600 * 24)

		log.Info('getactorlist|db')
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
