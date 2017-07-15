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

# [
# {"type": "add",
# "id": "av0000001",
# "fields": {"no":"SUJI-041", "actor":"Abigaile Johnson(Spunky Bee、Abby、Veronika、Petty)", "name":"金パイパンポルノ", "dur":120, "releaseyear": 2013, "releasemonth": 11, "releaseday": 19, "company": "乱者"}
# },
# {"type": "add",
# "id": "av0000002",
# "fields": {"no":"AOZ-145", "actor":"Abigaile Johnson(Spunky Bee、Abby、Veronika、Petty)", "name":"欧制服美少女 Abigaile J", "dur":110, "releaseyear": 2013, "releasemonth": 5, "releaseday": 24, "company": "青空ソフト"}
# }
# ]

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