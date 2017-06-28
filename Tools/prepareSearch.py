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

#
# def FixDB_Programs():
# #{
# 	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
# 	cur = conn.cursor()
#
# 	sSql = 'select id, number, name from programs'
# 	cur.execute(sSql)
# 	res = cur.fetchall()
#
# 	dictPrograms = {}
# 	for r in res:
# 	# {
# 		sName = r[2]
#
# 		# sName = sName.replace(u' ', '')
# 		sName = sName.replace(u'\u0000', '')
# 		sName = sName.strip()
# 		# if sName == r[2]:
# 		# 	continue
# 		dictPrograms[r[0]] = sName
# 	# }
#
# 	for (id, name) in dictPrograms.items():
# 	#{
# 		sSql = 'update programs set name="' + name + '" where id=' + str(id)
# 		print sSql
# 		cur.execute(sSql)
# 	#}
# 	conn.commit()
#
# 	cur.close()
# 	conn.close()
# #}

def FixDB_Programs():
#{
	f = open('/app/srv_api/cloudsearch_data/cs_all.json')
	sData = f.read()
	aryData = sData.split('},')
	f.close()

	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()
	nCount = 0
	for sItem in aryData:
	#{
		sItem = sItem + '}'
		sItem = sItem.replace('\r', '')
		sItem = sItem.replace('\n', '')

		sItem = sItem.replace('"}}}', '"}}')
		jsItem = json.loads(sItem)

		sSql = 'update programs set name="' + jsItem['fields']['name'] + '" where number="' + jsItem['fields']['no'] + '"'
		# print sSql
		cur.execute(sSql)
		# time.sleep(1)
		print nCount
		nCount += 1
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

	dictItem = {}
	for sItem in aryData:
	# {
		sItem = sItem + '}'
		sItem = sItem.replace('\r', '')
		sItem = sItem.replace('\n', '')

		sItem = sItem.replace('"}}}', '"}}')

		# print sItem
		jsItem = json.loads(sItem)
		dictItem[jsItem['fields']['no']] = jsItem
	# }

	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()

 	sSql = 'select id, number, name from programs'
 	cur.execute(sSql)
 	res = cur.fetchall()

 	for r in res:
 	#{
		if dictItem.has_key(r[1]):
		#{
			dictItem[r[1]]['fields']['id'] = r[0]
		#}
	#}
	cur.close()
	conn.close()

	f = open('/app/cs_id.json', 'w')
	f.write('[\n')
	for (no, data) in dictItem.items():
	#{
		f.write(json.dumps(data, ensure_ascii=False))
		f.write(',\n')
	#}
	f.write(']\n')
	f.close()
#}

if __name__ == '__main__':
#{
	# Main()
	# CreateActor()
	# ChangeProgramsTableActorToID()
	# MoveCoverFileOnS3()
	FixDB_Programs()
	# SplitAlias()
	# DisableRepeatedActor()
#}