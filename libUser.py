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
import mysql.connector

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
		# db = boto3.resource('dynamodb')
		# table = db.Table('avbus_users')
		# response = table.get_item(Key={'uid': self.m_jsProfile['uid']})
		# if response.has_key('Item'):
		# #{
		# 	item = response['Item']
		# 	self.m_jsProfile['point'] = item['point']
		# #}
		# else:
		# #{
		# 	# new user
		# 	table.put_item(Item={'uid': self.m_jsProfile['uid'], 'point': self.m_nNewUserPoint})
		# 	self.m_jsProfile['point'] = self.m_nNewUserPoint
		# #}


		conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
		cur = conn.cursor()
		try:
		# {
			sSql = 'select uid, point from users'
			cur.execute(sSql)
			res = cur.fetchall()

			bFound = False
			for r in res:
			# {
				self.m_jsProfile['point'] = r[1]
				bFound = True
				break
			# }
			if bFound is False:
			#{
				self.m_jsProfile['point'] = self.m_nNewUserPoint
				sCql = 'insert into users("uid", "point") values ("' + self.m_jsProfile['uid'] + '", %d)'%(self.m_nNewUserPoint)
				cur.execute(sCql)
			#}
			cur.close()
			conn.close()

		# }
		except:
		# {
			print 'load Profile failed'
			cur.close()
			conn.close()
		# }
	#}

	def SaveProfile(self):
	#{
		# db = boto3.resource('dynamodb')
		# table = db.Table('avbus_users')
        #
		# table.put_item(Item={'uid': self.m_jsProfile['uid'], 'point': self.m_jsProfile['point']})


		conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
		cur = conn.cursor()
		try:
		# {
			sSql = 'update users set point=%d'%(self.m_jsProfile['point']) + ' where uid="' + self.m_jsProfile['uid'] + '"'
			cur.execute(sSql)

			cur.close()
			conn.close()
		# }
		except:
		# {
			cur.close()
			conn.close()
		# }
	#}

	def GetPoint(self):
	#{
		return self.m_jsProfile['point']
	#}

	def UsePoint(self, nPoint):
	#{
		if self.m_jsProfile['point'] < nPoint:
		#{
			print 'point: %d'%(self.m_jsProfile['point'])
			return False
		#}
		self.m_jsProfile['point'] -= nPoint
		self.SaveProfile()
	#}
#}
