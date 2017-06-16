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
import boto3
# from libUser import CUser

def badWordFilter(sData):
#{
	sRet = sData
	aryBadWords = [
		['变态', '**'],
		['轮奸', '**'],
		['调教', '**'],
		['孕汁', '孕*'],
		['痴女', '**'],
		['巨乳', '**'],
		['调教', '**'],
		['尻', '*'],
		['中出', '**'],
		['FUCK', '****'],
		['拘束', '**'],
		['爆乳', '**'],
		['淫', '*'],
		['肛', '*'],
		['阴', '*'],
		['潮吹', '**'],
		['奴隶', '**'],
		['性奴', '**']
	]
	for bw in aryBadWords:
	#{
		sRet = sRet.replace(bw[0], bw[1])
	#}
	return sRet
#}

def _ISearch(sToken, sActor, sProgramName, nMaxCount, log):
	"""
	interface: get actor list(full)
	"""
#{
	csd = boto3.client('cloudsearchdomain', endpoint_url='http://search-avbus-h5ip3yilaxh457mgkbhhyehzre.ap-southeast-1.cloudsearch.amazonaws.com')

	aryData = []
	if sProgramName:
	#{
		res = csd.search(query=sProgramName, size=nMaxCount)
		# nFoundCount = res['hits']['found']

		for hit in res['hits']['hit']:
		#{
			# print '-----------------------------'
			# print hit['fields']
			# print hit['fields']['no'][0] + ' : ' + hit['fields']['actor'][0] + ' : ' + hit['fields']['name'][0]
			sName = badWordFilter(hit['fields']['name'][0])
			aryData.append({'no': hit['fields']['no'][0], 'actor': hit['fields']['actor'][0], 'name': sName})#hit['fields']['name'][0]})
		#}
		jsRet = {
			"result" : "+OK",
			"items": aryData
		}
		return json.dumps(jsRet, ensure_ascii=False)
	#}
	if sActor:
	#{
		res = csd.search(query=sActor, size=nMaxCount)
		for hit in res['hits']['hit']:
		# {
			#print hit['fields']['no'][0] + ' : ' + hit['fields']['actor'][0] + ' : ' + hit['fields']['name'][0]
			# print '-----------------------------'
			# print hit['fields']
			# print hit['fields']['no'][0] + ' : ' + hit['fields']['actor'][0] + ' : ' + hit['fields']['name'][0]
			aryData.append({'no': hit['fields']['no'][0], 'actor': hit['fields']['actor'][0], 'name': hit['fields']['name'][0]})

		# }
		jsRet = {
			"result" : "+OK",
			"items": aryData
		}
		return json.dumps(jsRet, ensure_ascii=False)
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
	print _ISearch(None, u'鲇川奈绪', u'美形な女子校生', 100, None)
#}