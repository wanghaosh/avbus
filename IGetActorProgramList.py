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
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import zlib

from libMemC import CMemCached
from libLog import CLog

from libUser import CUser

def _IGetActorProgramList(sActor, nPageIndex, nPageSize, log):
	"""
	interface: get one actor's program list
	param:
		actor: actor name
	"""
#{
	if sActor is None:
		return '{"result": "-ERR", "msg": "not fount parameter [actor]"}'

	sMode = 'mem'
	mem = CMemCached()
	sKey = 'api_getactorprogramlist_' + sActor
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
		sSql = 'select id, actor, name, dur, releaseYear, releaseMonth, releaseDay, company from programs where actor="' + sActor + '" limit %d, %d'%(nPageIndex * nPageSize, nPageSize)
		cur.execute(sSql)
		res = cur.fetchall()

		aryRecs = []
		for r in res:
		#{
			sName = r[2].replace('\r', '')
			sName = sName.replace('\n', '')
			sName = sName.replace('\t', '')
			sName = sName.strip()

			rec = {
				"id": r[0],
				"actor": r[1],
				"name": sName,
				"dur": r[3],
				"release": r[4],
				"company": r[7]
			}
			aryRecs.append(rec)
		#}
		cur.close()
		conn.close()
		jsRet = {
			"result":"+OK",
			"count": len(aryRecs),
			"programs": aryRecs
		}
		#}
		#except:
		#{
		#	cur.close()
		#	conn.close()
		#}
#		sRet = '{"result":"+OK", "actorcount":' + len(aryRecs) + ', "actors":' + str(aryRecs) + '}'
		sRet = json.dumps(jsRet, ensure_ascii=False)
		mem.Set(sKey, sRet, 3600 * 24)
	#}
	log.Info('getactorprogramlist|' + sMode)
	return sRet
#}
