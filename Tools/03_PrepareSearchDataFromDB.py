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

def Main():
#{
	f = open('/app/srv_api/cloudsearch_data/cs_all.json')
	sData = f.read()
	aryData = sData.split('},')
	f.close()

	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()

	sSql = 'select id, number, actor, name, dur, releaseYear, releaseMonth, releaseDay, company from programs'

	cur.execute(sSql)


	datas = cur.fetchall()

	nFIndex = 0
	sfn = 'dbR_%02d.txt'%(nFIndex)
	print sfn
	f = open(sfn, 'w')
	f.write('[')
	nCount = 0
	bFirst = True
	for r in datas:
	#{
		jsItem = {
			"fields": {
				"id": r[0],
				"no": r[1],
				"actor": r[2],
				"name": r[3],
				"dur": r[4],
				"releaseyear": r[5],
				"releasemonth": r[6],
				"releaseday": r[7],
				"company": r[8]
			},
			"type": "add",
			"id": "VB%08d"%(r[0])
		}
		if bFirst:
		#{
			f.write(',\n')
			bFirst = False
		#}
		f.write(json.dumps(jsItem, ensure_ascii=False))
		nCount += 1
		if nCount % 15000 == 0:
		#{
			nFIndex += 1
			f.write(']')
			f.close()

			sfn = 'dbR_%02d.txt' % (nFIndex)
			print sfn
			bFirst = True
			f = open(sfn, 'w')
			f.write('[')
		#}
	#}
	f.write(']')
	f.close()

	cur.close()
	conn.close()
#}


# [
# {"fields": {"releasemonth": 6, "name": "深夜夜行バス ゲリラ露出 大ひびき", "no": "NEO-042", "company": "レイディックス", "releaseday": 20, "actor": "大>响(大ひびき)", "releaseyear": 2014, "dur": 120, "id": 20185}, "type": "add", "id": "av0037346"},
# {"fields": {"releasemonth": 7, "name": "私のバタ犬 Maika", "no": "NEO-043", "company": "neo（パラドックス）", "releaseday": 20, "actor": "Maika", "releaseyear": 2014, "dur": 130, "id": 120725}, "type": "add", "id": "av0001114"},
# {"fields": {"releasemonth": 5, "name": "ザメン募集 急募！あなたの精子をペットボトルに溜めて下さい！ 小司あん", "no": "NEO-041", "company": "レイディック
# ス", "releaseday": 20, "actor": "平子知歌", "releaseyear": 2014, "dur": 145, "id": 108768}, "type": "add", "id": "av0056679"},
# {"fields": {"releasemonth": 11, "name": "痴女QUEEN 深田梨菜 BEST 4时间", "no": "DJSB-48", "company": "ジャネス", "releaseday": 5, "actor": "深田梨菜(ふ>かだりな)", "releaseyear": 2013, "dur": 240, "id": 85926}, "type": "add", "id": "av0099502"},

if __name__ == '__main__':
#{
	Main()
#}