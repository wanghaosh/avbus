#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
avbus555 web api service
"""

import json
import sys

import mysql.connector
import urllib2

# from libUser import CUser

def CreateActor():
#{
	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()
	try:
	# {
		sSql = 'select actor,count(*) from programs group by actor'
		cur.execute(sSql)
		res = cur.fetchall()

		# aryRecs = []
		dictActors = {}
		for r in res:
		# {
			dictActors[r[0]] = "https://s3-ap-southeast-1.amazonaws.com/avbus-data/covers/" + r[0] + ".jpg"
		# }

		#
		nCount = 0
		for (name, cover) in dictActors.items():
		#{
			sSql = 'insert into actors(name, cover_pic) values("' + name + '", "' + cover + '")'

			cur.execute(sSql)
			nCount += 1
			print str(nCount) + ' : ' + name
		#}
		conn.commit()

		cur.close()
		conn.close()

		jsRet = {
			"result": "+OK",
			"actorcount": len(aryRecs),
			"actors": aryRecs,
			"mode": "db"
		}
		sRet = json.dumps(jsRet, ensure_ascii=False)
		return sRet

		# return aryRecs
	# }
	except:
	# {
		cur.close()
		conn.close()

		return None
	# }
#}

def ChangeProgramsTableActorToID():
#{
	conn = mysql.connector.connect(user='avbus555', password='avbus555',host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()
	# sSql = 'select actor,count(*) from programs group by actor'
	sSql = 'select id, name from actors'
	cur.execute(sSql)
	res = cur.fetchall()

	# aryRecs = []
	dictActors = {}
	for r in res:
	# {
		dictActors[r[1]] = r[0]
	# }

	#
	nCount = 0
	for (name, id) in dictActors.items():
	# {
		sSql = 'update programs set actor_id=%d where actor="'%(id) + name + '"'
		print sSql
		# sSql = 'insert into actors(name, cover_pic) values("' + name + '", "' + cover + '")'

		cur.execute(sSql)
		# nCount += 1
		# print str(nCount) + ' : ' + name
	# }
	conn.commit()

	cur.close()
	conn.close()

	# jsRet = {
	# 	"result": "+OK",
	# 	"actorcount": len(aryRecs),
	# 	"actors": aryRecs,
	# 	"mode": "db"
	# }
	# sRet = json.dumps(jsRet, ensure_ascii=False)
	# return sRet

#}

if __name__ == '__main__':
#{
	# CreateActor()
	ChangeProgramsTableActorToID()
#}