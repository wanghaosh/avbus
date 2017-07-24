#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
avbus555 web api service
"""

import json
# import base64
import datetime
# import time
# import urllib2
# import urllib
import sys

from gevent import monkey
# from gevent.pywsgi import WSGIServer
# monkey.patch_all()

# import mysql.connector
# from Crypto.Cipher import AES
# from binascii import b2a_hex, a2b_hex

# from libMemC import CMemCached
from libLog import CLog
import boto3
# import mysql.connector

################################
# from flask import Flask
# from flask import request
#
# app = Flask(__name__)

# g_log = CLog()
# g_log.Init('/logs/avbus_api.log', '1')

# from cassandra.cluster import Cluster
# from cassandra.policies import DCAwareRoundRobinPolicy

class CUser:
#{
	def __init__(self, sUid):
	#{
		# self.m_sBucket = 'avline-data'
		self.m_jsProfile = {
			'uid': sUid,
			'point': 0,
			'lastUsePointDT': 20000101,
			# 'no_view_count': 0
		}
		self.m_nNewUserPoint = 10
		self.LoadProfile()
	#}

	def LoadProfile(self):
	#{
		db = boto3.resource('dynamodb')
		table = db.Table('avbus_users')
		response = table.get_item(Key={'uid': self.m_jsProfile['uid']})
		if response.has_key('Item'):
		#{
			item = response['Item']
			self.m_jsProfile['point'] = item['point']
			if item.has_key('lastUsePointDT'):
			#{
				self.m_jsProfile['lastUsePointDT'] = item['lastUsePointDT']
			#}
			print 'load from dynamodb: ' + str(self.m_jsProfile)
		#}
		else:
		#{
			# new user
			table.put_item(Item={'uid': self.m_jsProfile['uid'], 'point': self.m_nNewUserPoint})
			self.m_jsProfile['point'] = self.m_nNewUserPoint

			print 'new user dynamodb: ' + str(self.m_jsProfile)
		#}
	#}

	def SaveProfile(self):
	#{
		db = boto3.resource('dynamodb')
		table = db.Table('avbus_users')

		table.put_item(Item={'uid': self.m_jsProfile['uid'], 'point': self.m_jsProfile['point']})
	#}

	def GetPoint(self):
	#{
		return self.m_jsProfile['point']
	#}

	def UsePoint(self, nPoint):
	#{
		# 检查最后一次使用积分的时间，如果是前一天则自动将积分补足
		dateNow = datetime.datetime.now()
		lNow = dateNow.year * 10000 + dateNow.month * 100 + dateNow.day

		if self.m_jsProfile['lastUsePointDT'] != lNow:
		#{
			print 'new days , set point = 10 : ' + self.m_jsProfile['uid']
			self.m_jsProfile['point'] = 10
		#}

		if self.m_jsProfile['point'] < nPoint:
		#{
			print 'point: %d'%(self.m_jsProfile['point'])
			return False
		#}
		self.m_jsProfile['point'] -= nPoint
		self.SaveProfile()
	#}
#}
