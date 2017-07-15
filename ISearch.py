#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
avbus555 web api service
"""

import json
import sys

import mysql.connector
from libWordFilter import CWordFilter
import boto3

from libMemC import CMemCached

def _ISearch(sToken, sActor, sProgramName, nMaxCount, log):
	"""
	interface: get actor list(full)
	"""
#{
	csd = boto3.client('cloudsearchdomain', endpoint_url='http://search-avbus-v1-gnsia355htzip3dgfvzas52rda.ap-southeast-1.cloudsearch.amazonaws.com')

	if sProgramName:
	#{
		return _searchProgram(sProgramName, nMaxCount, csd)
	#}
	if sActor:
	#{
		return _searchActor(sActor, nMaxCount, csd)
	#}
	jsRet = {
		"result" : "+OK",
		"items": aryData
	}
	sRet = json.dumps(jsRet, ensure_ascii=False)
	return sRet

	# return '{"result": "-ERR", "msg": "Not Found Data."}'
#}

def _searchProgram(sKeyword, nMaxCount, csd):
#{
	res = csd.search(query=sKeyword, queryOptions='{"fields": ["name"]}', size=nMaxCount)

	aryData = []

	for hit in res['hits']['hit']:
	# {
		sName = CWordFilter.badWordFilter(hit['fields']['name'][0])
		# sID = hit['fields']['id'][0]
		sID = hit['fields']['no'][0]
		aryData.append({'no': sID, 'actor': hit['fields']['actor'][0], 'name': sName})  # hit['fields']['name'][0]})
	# }
	jsRet = {
		"result" : "+OK",
		"items": aryData
	}
	sRet = json.dumps(jsRet, ensure_ascii=False)
	return sRet
#}

def _searchActor(sKeyword, nMaxCount, csd):
#{
	mem = CMemCached()
	sKey = 'searchactor_' + sKeyword + '_%d'(nMaxCount)
	sKey = sKey.encode('utf-8')
	sRet = mem.Get(sKey)
	if sRet:
	#{
		sRet = sRet.replace('"mode": "db"', '"mode": "mem"')
		return sRet
	#}

	res = csd.search(query=sKeyword, queryOptions='{"fields": ["actor"]}', size=nMaxCount * 10)

	# aryData = []
	# 先搜索节目
	dictProgramIDs = {}
	for hit in res['hits']['hit']:
	# {
		sName = CWordFilter.badWordFilter(hit['fields']['name'][0])
		# sID = hit['fields']['id'][0]
		sID = hit['fields']['id'][0]
		# aryData.append({'no': sID, 'actor': hit['fields']['actor'][0], 'name': sName})  # hit['fields']['name'][0]})
		if dictProgramIDs.has_key(sID) is False:
		#{
			dictProgramIDs[sID] = {}
			dictProgramIDs[sID]['count'] = 0
		#}
		dictProgramIDs[sID]['pid'] = sID
		dictProgramIDs[sID]['count'] += 1
	# }

	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()  # 从数据库中取出这些节目对应的演员id

	aryActors = []
	dictActorIDs = {}
	for (sID, v) in dictProgramIDs.items():
	#{
		print ' '
		print ' '
		print '-------------'
		sSql = 'select number, actor_id from programs where id=' + str(v['pid'])
		print sSql

		cur.execute(sSql)
		res = cur.fetchall()

		for r in res:
		#{
			aid = r[1]
			if dictActorIDs.has_key(aid):
			#{
				break
			#}
			dictActorIDs[aid] = True
			sSql = 'select id, name, alias, program_count from actors where id=' + str(aid)
			print '    -> ' + sSql
			cur.execute(sSql)
			res = cur.fetchall()
			for r in res:
			#{
				rec = {
					"id": r[0],
					"actor": r[1],
					"alias": r[2],
					"pic": "https://s3-ap-southeast-1.amazonaws.com/avbus-data/covers/%d.jpg" % (r[0]),
					"programcount": r[3]
				}
				# print rec
				aryActors.append(rec)
			#}
			break
		#}
	#}

	cur.close()
	conn.close()

	jsRet = {
		"result": "+OK",
		"actorcount": len(aryActors),
		"actors": aryActors,
		"mode": "db"
	}
	sRet = json.dumps(jsRet, ensure_ascii=False)
	mem.Set(sKey, sRet, 3600 * 24)
	return sRet
#}

#-------------------------------------------------------#
if __name__ == '__main__':
#{
	print _ISearch(None, u'鲇川奈绪', u'美形な女子校生', 100, None)
#}