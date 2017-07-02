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


def SumProgramCount():
#{
	conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
	cur = conn.cursor()
	sSql = 'select actor_id, count(*) from programs group by actor_id'
	cur.execute(sSql)
	res = cur.fetchall()

	dictActors = {}
	for r in res:
	#{
		dictActors[r[0]] = r[1]
	#}

	for (id, count) in dictActors.items():
	#{
		sSql = 'update actors set program_count=' + str(count) + ' where id=' + str(id)
		print sSql
		cur.execute(sSql)
	#}
	conn.commit()

	cur.close()
	conn.close()
#}

if __name__ == '__main__':
#{
	# CreateActor()
	# ChangeProgramsTableActorToID()
	# MoveCoverFileOnS3()
	# FixDB_Programs()
	# SplitAlias()
	# DisableRepeatedActor()
	SumProgramCount()
#}