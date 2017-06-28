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
from libAES import encrypt
from libAES import decrypt
from libWordFilter import CWordFilter
from libMemC import CMemCached
from libLog import CLog
import boto3
# from libUser import CUser
#
# def badWordFilter(sData):
# #{
# 	sRet = sData
# 	aryBadWords = [
# 		[u'变态', '**'],
# 		[u'轮奸', '**'],
# 		[u'调教', '**'],
# 		[u'孕汁', '**'],
# 		[u'痴女', '**'],
# 		[u'巨乳', '**'],
# 		[u'调教', '**'],
# 		[u'尻', '*'],
# 		[u'中出', '**'],
# 		[u'FUCK', '****'],
# 		[u'拘束', '**'],
# 		[u'爆乳', '**'],
# 		[u'淫', '*'],
# 		[u'肛', '*'],
# 		[u'阴', '*'],
# 		[u'潮吹', '**'],
# 		[u'奴隶', '**'],
# 		[u'性奴', '**'],
# 		[u'监禁', '**']
# 	]
# 	for bw in aryBadWords:
# 	#{
# 		# print bw
# 		sRet = sRet.replace(bw[0], bw[1])
# 	#}
# 	return sRet
# #}

def _ISearch(sToken, sActor, sProgramName, nMaxCount, log):
	"""
	interface: get actor list(full)
	"""
#{
	csd = boto3.client('cloudsearchdomain', endpoint_url='http://search-avbus-v1-gnsia355htzip3dgfvzas52rda.ap-southeast-1.cloudsearch.amazonaws.com')

	aryData = []
	if sProgramName:
	#{
		res = csd.search(query=sProgramName, size=nMaxCount)
		# nFoundCount = res['hits']['found']

		for hit in res['hits']['hit']:
		#{
			# print '-----------------------------'
			print hit['fields']
			# print hit['fields']['no'][0] + ' : ' + hit['fields']['actor'][0] + ' : ' + hit['fields']['name'][0]
			sName = CWordFilter.badWordFilter(hit['fields']['name'][0])
			sID = hit['fields']['id'][0]
			sNo = hit['fields']['no'][0]
			sNo = encrypt(sNo, 'avbus555fhzidian')
			aryData.append({'id': sID, 'no': sNo, 'actor': hit['fields']['actor'][0], 'name': sName})#hit['fields']['name'][0]})
		#}
		jsRet = {
			"result" : "+OK",
			"items": aryData
		}
		sRet = json.dumps(jsRet, ensure_ascii=False)
		return sRet
	#}
	if sActor:
	#{
		res = csd.search(query=sActor, size=nMaxCount)
		for hit in res['hits']['hit']:
		# {
			#print hit['fields']['no'][0] + ' : ' + hit['fields']['actor'][0] + ' : ' + hit['fields']['name'][0]
			# print '-----------------------------'
			print hit['fields']
			# print hit['fields']['no'][0] + ' : ' + hit['fields']['actor'][0] + ' : ' + hit['fields']['name'][0]
			sName = CWordFilter.badWordFilter(hit['fields']['name'][0])
			sID = hit['fields']['id'][0]
			sNo = hit['fields']['no'][0]
			sNo = encrypt(sNo, 'avbus555fhzidian')
			aryData.append({'id', sID, 'no': sNo, 'actor': hit['fields']['actor'][0], 'name': sName})# hit['fields']['name'][0]})

		# }
		jsRet = {
			"result" : "+OK",
			"items": aryData
		}
		sRet = json.dumps(jsRet, ensure_ascii=False)
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
	print _ISearch(None, u'鲇川奈绪', u'美形な女子校生', 100, None)
#}