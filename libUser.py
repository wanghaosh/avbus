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

# import mysql.connector
# from Crypto.Cipher import AES
# from binascii import b2a_hex, a2b_hex

# from libMemC import CMemCached
from libLog import CLog
import boto3

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
			'point': 0
			# 'no_view_count': 0
		}
		self.m_nNewUserPoint = 10
		self.LoadProfile()
	#}

	def LoadProfile(self):
	#{
		# s3 = boto3.client('s3')
		# sKey = 'users/' + self.m_jsProfile['uid']
		# try:
		# #{
		# 	response = s3.get_object(Bucket=self.m_sBucket, Key=sKey)
		# 	rs = response['Body']
        #
		# 	sData = rs.read()
		# 	self.m_jsProfile = json.loads(sData)
		# #}
		# except:
		# #{
		# 	print 'Not Found User Profile'
		# #}


		# cluster = Cluster(['172.31.7.146'], load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='datacenter1'))
		# conn = cluster.connect()
		# try:
		# #{
		# 	conn.execute('use avbus')
		# 	sCql = "select uid, point from users where uid='" + self.m_jsProfile['uid'] + "'"
		# 	datas = conn.execute(sCql)
		# 	if len(datas) > 0:
		# 	#{
		# 		for data in datas:
		# 		#{
		# 			self.m_jsProfile['point'] = data.point
		# 			break
		# 		#}
		# 	#}
		# 	else:
		# 	#{
		# 		# new user
		# 		sCql = "insert into users (uid, point) values ('" + self.m_jsProfile['uid'] + "', %d)"%(self.m_nNewUserPoint)
		# 		self.m_conn.execute(sCql)
		# 		self.m_jsProfile['point'] = nNewUserPoint
		# 	#}
		# 	cluster.shutdown()
		# #}
		# except:
		# #{
		# 	print 'Except: LoadProfile[' + str(self.m_jsProfile) + ']'
		# #}
		# finally:
		# #{
		# 	cluster.shutdown()
		# #}

		db = boto3.resource('dynamodb')
		table = db.Table('avbus_users')
		response = table.get_item(Key={'uid': self.m_jsProfile['uid']})
		if response.has_key('Item'):
		#{
			item = response['Item']
			self.m_jsProfile['point'] = item['point']
		#}
		else:
		#{
			# new user
			table.put_item(Item={'uid': self.m_jsProfile['uid'], 'point': self.m_nNewUserPoint})
			self.m_jsProfile['point'] = self.m_nNewUserPoint
		#}
	#}

	def SaveProfile(self):
	#{
		# s3 = boto3.client('s3')
		# sKey = 'users/' + self.m_jsProfile['uid']
		# s3.put_object(Bucket=self.m_sBucket, Key=sKey, Body=json.dumps(self.m_jsProfile), ACL='public-read', ContentType='text/html')


		# cluster = Cluster(['172.31.7.146'], load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='datacenter1'))
		# conn = cluster.connect()
		# try:
		# #{
		# 	conn.execute('use avbus')
		# 	sCql = "insert into users (uid, point) values ('" + self.m_jsProfile['uid'] + "', %d)"%(self.m_jsProfile['point'])
		# 	conn.execute(sCql)
		# #}
		# except:
		# #{
		# 	print 'Except: SaveProfile[' + str(self.m_jsProfile) + ']'
		# #}
		# finally:
		# #{
		# 	cluster.shutdown()
		# #}


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
		if self.m_jsProfile['point'] < nPoint:
			return False
		self.m_jsProfile['point'] -= nPoint
		self.SaveProfile()
	#}
#}
