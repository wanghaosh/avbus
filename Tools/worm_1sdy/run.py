#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wang.hao'

import os
import sys
import shutil
import glob
import json
import commands
#from cassandra.cluster import Cluster

# from cassandra.cluster import Cluster
# from cassandra.policies import DCAwareRoundRobinPolicy
# import mysql.connector

import datetime
#import memcache
import time
import urllib2
import urllib

# sys.path.append('/app/srv_libs/')
# from libSetting import CSetting
# from libLog import CLog

import subprocess

# from libS3 import CS3Bucket
# import boto
import boto3
# import botocore
import traceback
from libOneActor import COneActor
# g_log = CLog()
# g_log.Init('/logs/cdnChecker.log', '1')

import mysql.connector
g_conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
g_cur = g_conn.cursor()
g_mysql = [g_conn, g_cur]
#
s3 = boto3.resource('s3')

class C1sdy:
#{
	def __init__(self):
	#{
		self.m_sBaseURI = 'http://www.1sdy.com/topiclist/'
		self.m_dictActors = {}
	#}

	def GetAllPage(self):
	#{
		# for nPageName in range(86, 513):
		for nPageName in range(86, 88):
		#{
			a = COneActor(nPageName, g_mysql, s3, '/app/srv_api/Tools/worm_1sdy/data/')
			a.GetAndParse()
			# break
		#}
	#}
#}

def ImportDataToProductEnv():
#{

	sDir = '/app/pics/'
	pics = os.listdir(sDir)
	dictData = {}
	for sFn in pics:
	# {
		if sFn.find('.json') < 0:
			continue
		sLocalFn = sDir + sFn
		aryTmp = sLocalFn.replace('.json', '').split('_')
		sActor = aryTmp[0]
		sNo = aryTmp[1]

		f = open(sLocalFn)
		sData = f.read()

		f.close()
		jsData = json.loads(sData)

		if dictData.has_key(sActor) is False:
		#{
			# dictData[sActor]['']
			dictData[sActor]['programs'] = []
		#}
		dictData[sActor]['programs'].append(
			{
				"no": sNo,
				"cover": jsData['cover'],
				"name": jsData['name'].replace('别名：', ''),
				'dt': jsData['dt'].replace('年份：', '年'),
				'detail': jsData['detail']
			}
		)
	# }
#}

if __name__ == '__main__':
#{
	site = C1sdy()
	site.GetAllPage()
#}


