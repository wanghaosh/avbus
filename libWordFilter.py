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

from libMemC import CMemCached
from libLog import CLog
import boto3
# from libUser import CUser

class CWordFilter:
#{
	@staticmethod
	def badWordFilter(sData):
	#{
		sRet = sData
		aryBadWords = [
			[u'变态', '**'],
			[u'轮奸', '**'],
			[u'调教', '**'],
			[u'孕汁', '**'],
			[u'痴女', '**'],
			[u'巨乳', '**'],
			[u'调教', '**'],
			[u'尻', '*'],
			[u'中出', '**'],
			[u'FUCK', '****'],
			[u'拘束', '**'],
			[u'爆乳', '**'],
			[u'淫', '*'],
			[u'肛', '*'],
			[u'阴', '*'],
			[u'潮吹', '**'],
			[u'奴隶', '**'],
			[u'性奴', '**'],
			[u'监禁', '**']
		]
		for bw in aryBadWords:
		#{
		# print bw
			sRet = sRet.replace(bw[0], bw[1])
		#}
		return sRet
	#}
#}
