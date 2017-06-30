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

g_conn = mysql.connector.connect(user='avbus555', password='avbus555', host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com', database='avbus')
g_cur = g_conn.cursor()
g_mysql = [g_conn, g_cur]
#
# s3 = boto3.resource('s3')

class C1sdy:
#{
	def __init__(self):
	#{
		self.m_sBaseURI = 'http://www.1sdy.com/topiclist/'
		self.m_dictActors = {}
	#}

	def GetAllPage(self):
	#{
		for nPageName in range(86, 513):
		#{
			a = COneActor(nPageName, g_mysql)
			a.GetAndParse()
			break
		#}
	#}
    #
	# def GetOnePage(self, sPageName):
	# #{
	# 	print '-------------------------------'
	# 	sUri = self.m_sBaseURI + sPageName
	# 	print sUri
	# 	sCmd = 'curl -o "' + sPageName + '" --referer "http://www.1sdy.com" "' + sUri + '" -A "Mozilla/5.0 (Windows NT 6.1)"'
	# 	print sCmd
	# 	os.system(sCmd)
    #
	# 	#
	# 	sData = CHttp.HttpGet(sUri)
	# 	# print sData
	# 	sActor = sData.split('<title>')[1].split('所有作品番号')[0]
	# 	# print sActor
	# 	sPic = sData.split('.html"><img src="')[1].split('">')[0]
	# 	# print '    -> ' + sPic
    #
	# 	sDetail = sData.split('简介</a>')[1].split('</div>')[0].replace('<br />', '\n').replace('<div class="u">', '').replace('</br>', '')
	# 	# print sDetail
    #
	# 	nActorID = self.AddActor(sActor, sPic, sDetail)
    #
	# 	aryProgramsTmp = sData.split('<div class="showPlay">')[1].split('<a href="')#.split('.html" target="_blank"><img src="')
	# 	for sTmp in aryProgramsTmp:
	# 	#{
	# 		aryTmp = sTmp.split('" target="_blank"><img src="')
	# 		if len(aryTmp) <= 1:
	# 			continue
	# 		sDetailPageUri = 'http://www.1sdy.com' + aryTmp[0]
    #
	# 		sOneProgram = aryTmp[1].split('"></a>')[0]
	# 		aryTmp = sOneProgram.split('" alt="')
	# 		sCoverPic = aryTmp[0]
	# 		sNo = aryTmp[1].split(' ')[1]
    #
	# 		self.GetProgramDetailPage(sDetailPageUri, nActorID, sActor, sNo, sCoverPic)
	# 	#}
	# 	sTmp = sData.split('页次:')[1].split('页')[0]
	# 	nCurPage = int(sTmp.split('/')[0])
	# 	nTotalPage = int(sTmp.split('/')[1])
	# 	print '[%d / %d]'%(nCurPage, nTotalPage)
	# 	if nCurPage >= nTotalPage:
	# 		return -1
	# 	return nCurPage + 1
	# #}
    #
	# def GetProgramDetailPage(self, sUri, nActorID, sActor, sNo, sCoverPic):
	# #{
	# 	sData = CHttp.HttpGet(sUri)
	# 	sData = sData.replace('\r', '').replace('\n', '').replace('<br>', '').replace('<p>', '')
	# 	aryTmp = sData.split('<li class="small">')
	# 	# for sTmp in aryTmp:
	# 	# #{
	# 	# 	print sTmp
	# 	# #}
	# 	sDT = aryTmp[3].replace('</li>', '')
	# 	sName = aryTmp[7].replace('</li>', '')#.replace('\n', '')
	# 	sInfo = sData.split('<div class="showInfo">')[1].split('</div>')[0]
    #
	# 	self.AddProgram(nActorID, sActor, sName.strip(' '), sNo, sCoverPic, sInfo.strip(' '), sDT.strip(' '))
	# #}
    #
	# def AddActor(self, sActor, sActorPic, sDetail, cur, conn):
	# #{
	# 	print sActor + ' : ' + sActorPic
	# 	# print '  -> ' + sDetail
	# 	if self.m_dictActors.has_key(sActor) is False:
	# 	#{
	# 		self.m_dictActors[sActor] = {}
	# 	#}
	# 	self.m_dictActors[sActor]['pic'] = sActorPic
	# 	self.m_dictActors[sActor]['detail'] = sDetail
	# 	if self.m_dictActors[sActor].has_key('programs') is False:
	# 	#{
	# 		self.m_dictActors[sActor]['programs'] = []
	# 	#}
    #
	# 	# 查询数据库中是否有同名演员（有，补充信息&获取id；无，新增记录获得id）
	# 	sSql = 'select id from actors where name="' + sActor + '" and status=1'
	# 	cur.execute(sSql)
	# 	res = cur.fetchall()
	# 	nID = 0
	# 	for r in res:
	# 	#{
	# 		nID = r[0]
	# 		break
	# 	#}
	# 	if nID > 0:
	# 	#{
	# 		sSql = 'update actors set detail="' + sDetail + '" where id=' + str(nID)
	# 		print sSql
	# 		cur.execute(sSql)
	# 		conn.commit()
	# 	#}
	# 	else:
	# 	#{
	# 		# 数据库中没有同名演员
	# 		sSql = 'insert into actors(name, alias, detail, cover_pic, status, program_count, src_site) values("' + sActor + '", "-", "' + sDetail + '", "' + sActorPic + '", 1, 0, "www.1sdy.com")'
	# 		print sSql
	# 		cur.execute(sSql)
	# 		conn.commit()
    #
	# 		cur.execute('select @@IDENTITY')
	# 		res = cur.fetchall()
	# 		for r in res:
	# 		#{
	# 			nID = r[0]
	# 			break
	# 		#}
	# 	#}
    #
    #
	# 	# 下载人物图&上传到S3
	# 	sCmd = 'curl -o "' + sActor + '_%d.jpg" --referer "http://www.1sdy.com" "'%(nID) + sActorPic + '" -A "Mozilla/5.0 (Windows NT 6.1)"'
	# 	print sCmd
	# 	os.system(sCmd)
    #
	# 	s3.Object('avbus-data', 'covers2/%d.jpg' % (nID)).put(Body=open(sActor + '_%d.jpg' % (nID), 'rb'), ACL='public-read')
    #
	# 	return nID
	# #}
    #
	# def AddProgram(self, sActor, sProgramName, sProgramNo, sProgramCover, sProgramDetail, sDT):
	# #{
	# 	print '  -> [' + sProgramNo + '] ' + sDT + ' / ' + sProgramName
	# 	dictProgram = {
	# 			'name': sProgramName.strip(' '),
	# 			'no': sProgramNo.strip(' '),
	# 			'cover': sProgramCover.strip(' '),
	# 			'detail': sProgramDetail.strip(' '),
	# 			'dt': sDT.strip(' ')
	# 		}
    #
	# 	self.m_dictActors[sActor]['programs'].append(dictProgram)
    #
	# 	# download program cover
	# 	sCmd = 'curl -o "' + sActor + '_' + sProgramNo + '.jpg" --referer "http://www.1sdy.com" "' + sProgramCover + '" -A "Mozilla/5.0 (Windows NT 6.1)"'
	# 	print sCmd
	# 	os.system(sCmd)
    #
	# 	f = open(sActor + '_' + sProgramNo + '.json', 'w')
	# 	f.write(json.dumps(dictProgram, ensure_ascii=False))
	# 	f.close()
	# #}
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
		# s3.Object('avbus-data', 'covers/' + sLocalFn).put(Body=open(sDir + sFn, 'rb'), ACL='public-read')

		# step.1 write to MySQL
		# sSql = 'insert into actors(name, alias, cover_pic, status, program_count'

		# step.2 upload pic to S3
	# }
#}

if __name__ == '__main__':
#{
	site = C1sdy()
	site.GetAllPage()
#}


