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
# from libUser import CUser
reload(sys)
sys.setdefaultencoding('utf8')

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

def MoveCoverFileOnS3():
#{
	s3 = boto3.resource('s3')
	sDir = '/app/pics/'

	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()

	sSql = 'select id, name from actors'
	cur.execute(sSql)
	res = cur.fetchall()

	dictActors = {}
	for r in res:
	# {
		dictActors[r[1]] = r[0]
	# }
	cur.close()
	conn.close()

	# nCount = 0
	for (name, id) in dictActors.items():
	# {
		sFn = sDir + name + '.jpg'
		print sFn
		try:
		#{
			s3.Object('avbus-data', 'covers/%d.jpg'%(id)).put(Body=open(sFn, 'rb'), ACL='public-read')
		#}
		except:
		#{
			print "~~~~~~~~~~~~~~~!@@@@@@"
		#}
	# }

#}

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
	# 	sNumber = r[1]
    #
	# 	sNumber = sNumber.replace('⇥', '')
	# 	sNumber = sNumber.strip()
	# 	if sNumber == r[1]:
	# 	#{
	# 		continue
	# 	#}
	# 	dictPrograms[r[0]] = sNumber
		sName = r[2]#.decode("utf-8").encode("gbk")

		sName = sName.replace('&rsquo;', '')
		sName = sName.strip()
		if sName == r[2]:
			continue
		dictPrograms[r[0]] = sName
	# }

	for (id, name) in dictPrograms.items():
	#{
		# sSql = 'update programs set number="' + number + '" where id=' + str(id)
		sSql = 'update programs set name="' + name + '" where id=' + str(id)
		print sSql
		# cur.execute(sSql)
	#}
	conn.commit()

	cur.close()
	conn.close()
#}
#
# def DisableRepeatedActor():
# #{
# 	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
# 	cur = conn.cursor()
# 	sSql = 'select number, count(*) from programs group by number;'
# 	cur.execute(sSql)
# 	res = cur.fetchall()
#
# 	dictPrograms = {}
# 	for r in res:
# 	#{
# 		if r[1] <= 1:
# 		#{
# 			continue
# 		#}
# 		dictPrograms[r[0]] = r[1]
# 	#}
#
# 	dictActors = {}
# 	for (sNumber, nCount) in dictPrograms.items():
# 	#{
# 		sSql = 'update actors set status=0 where id=' +
# 	#}
# #}

def SplitAlias():
#{
	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()
	sSql = 'select id, name from actors'
	cur.execute(sSql)
	res = cur.fetchall()

	dictActors = {}
	for r in res:
	#{
		aryName = r[1].split('(')
		sName = aryName[0]
		sAlias = ''
		if len(aryName) > 1:
		#{
			sAlias = aryName[1]
		#}
		dictActors[r[0]] = [sName, sAlias]
	#}

	for (id, aryName) in dictActors.items():
	#{
		sSql = 'update actors set name="' + aryName[0] + '", alias="' + aryName[1] + '" where id=' + str(id)
		print sSql
	#}
#}

if __name__ == '__main__':
#{
	# CreateActor()
	# ChangeProgramsTableActorToID()
	# MoveCoverFileOnS3()
	# FixDB_Programs()
	SplitAlias()
#}