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
# import zlib
import urllib2
# import urllib

from libMemC import CMemCached
from libLog import CLog

# from libUser import CUser
import boto3
from boto3.dynamodb.conditions import Key, Attr

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

def getFromDynamoDB():
#{
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('avbus_programs')

	response = table.scan(FilterExpression = Attr('releaseYear').eq(2014))
	items = response['Items']
	#print items
	jsRet = {
		"result": "+OK",
		"programs": items
	}
	sRet = json.dumps(jsRet, ensure_ascii=False)
	#sRet = '-'
	return sRet
	# # }
	# except:
	# # {
	# 	return None
	# # }
#}

def getFromRDS(nYear, nPageIndex, nPageSize):
#{
	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()
	try:
	# {
		sSql = 'select count(*) from programs where releaseYear=%d'%(nYear)
		cur.execute(sSql)
		res = cur.fetchall()
		nTotalCount = 0
		for r in res:
		#{
			nTotalCount = r[0]
			break
		#}
		sSql = 'select id, actor, name from programs where releaseYear=%d limit %d,%d'%(nYear, nPageIndex * nPageSize, nPageSize)
		cur.execute(sSql)
		res = cur.fetchall()

		aryRecs = []
		for r in res:
		# {
			rec = {
				"id": r[0],
				"actor": r[1],
				"pic": "https://s3-ap-southeast-1.amazonaws.com/avbus-data/covers/" + r[1] + ".jpg"
			}
			aryRecs.append(rec)
		# }

		cur.close()
		conn.close()

		jsRet = {
			"result": "+OK",
			"year": nYear,
			"totalcount": nTotalCount,
			"pageindex": nPageIndex,
			"pagesize": nPageSize,
			"programs": aryRecs,
			"mode": "db"
		}
		sRet = json.dumps(jsRet, ensure_ascii=False)
		return sRet

		# return aryRecs
	# }
	except:
	# {
		cur.close()
		conn.close()

		return None
	# }
#}

def _IGetYearsProgramList(sToken, nYear, nPageIndex, nPageSize, log):
	"""
	interface
	"""
#{
	# mem = CMemCached()
	# sKey = 'api_getactorlist'
	# sKey = sKey.encode('utf-8')
    #
	# sRet = getFromMemcached(mem, sKey)
	# if sRet:
	# #{
	# 	jsRet = json.loads(sRet)
	# 	jsRet['mode'] = 'mem'
    #
	# 	log.Info('getactorlist|mem')
	# 	return json.dumps(jsRet, ensure_ascii=False)
	# #}
    #
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

	# sRet = getFromDynamoDB()
	# if sRet:
	# #{
	# 	# mem.Set(sKey, sRet, 3600 * 24)
    #
	# 	log.Info('_IGetYearsProgramList|db')
	# 	return sRet
	# #}

	sRet = getFromRDS(nYear, nPageIndex, nPageSize)
	if sRet:
	#{
		# mem.Set(sKey, sRet, 3600 * 24)

		log.Info('_IGetYearsProgramList|db')
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

#-------------------------------------------------------#
if __name__ == '__main__':
#{
	print getFromDynamoDB()
#}