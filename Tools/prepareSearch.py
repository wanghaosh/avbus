#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
avbus555 web api service
"""

import json
import sys
import os

import mysql.connector
import urllib2
import boto3
import time
# from libUser import CUser
reload(sys)
sys.setdefaultencoding('utf8')


def FixDB_Programs():
#{
	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()

	sSql = 'select id, number, name from programs'
	cur.execute(sSql)
	res = cur.fetchall()

	dictPrograms = {}
	for r in res:
	# {
		sName = r[2]

		# sName = sName.replace(u' ', '')
		sName = sName.replace(u'\u0000', '')
		sName = sName.strip()
		# if sName == r[2]:
		# 	continue
		dictPrograms[r[0]] = sName
	# }

	for (id, name) in dictPrograms.items():
	#{
		sSql = 'update programs set name="' + name + '" where id=' + str(id)
		print sSql
		cur.execute(sSql)
	#}
	conn.commit()

	cur.close()
	conn.close()
#}

def Main():
#{
	f = open('/app/srv_api/cloudsearch_data/cs_all.json')
	sData = f.read()
	aryData = sData.split('},')
	f.close()

	for sItem in aryData:
	#{
		sItem = sItem + '}'
		sItem = sItem.replace('\r', '')
		sItem = sItem.replace('\n', '')

		jsItem = json.loads(sItem)
		print jsItem
		time.sleep(1)
	#}
#}

if __name__ == '__main__':
#{
	# CreateActor()
	# ChangeProgramsTableActorToID()
	# MoveCoverFileOnS3()
	FixDB_Programs()
	# SplitAlias()
	# DisableRepeatedActor()
#}