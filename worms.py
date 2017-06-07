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
import mysql.connector

import datetime
#import memcache
import time
import urllib2
import urllib

# sys.path.append('/app/srv_libs/')
# from libSetting import CSetting
# from libLog import CLog

import subprocess

from libS3 import CS3Bucket
# import boto
import boto3
# import botocore

# g_log = CLog()
# g_log.Init('/logs/cdnChecker.log', '1')

class CHttp:
#{
	@staticmethod
	def HttpGet(sUri):
	#{
		# try:
		# #{
		resp = urllib2.urlopen(sUri)

		if resp.getcode() != 200:
		#{
			print resp.getcode()
			return None
		#}
		return resp.read()
		#}
		# except:
		# #{
	 #		info = sys.exc_info()
	 #		print info 
	 #		return None
		# #}
	#}

	@staticmethod
	def HttpPost(sUri, dictData):
	#{
		sDataEncode = urllib.urlencode(dictData)
		req = urllib2.Request(url = sUri, data=sDataEncode)
		resp = urllib2.urlopen(req)
		if resp.getcode() != 200:
		#{
			return None
		#}
		return resp.read()
	#}
#}

# def GetOnePage():
# #{
	
# #}

def DownloadIndexPage():
#{
	sCmd = 'curl -o 1.html "http://www.99fanhao.com/daquan/" -A "Mozilla/5.0 (Windows NT 6.1)"'
	os.system(sCmd)
	
	for n in range(2, 205):
	#{
		sCmd = 'curl -o %d.html "http://www.99fanhao.com/daquan/index_%d.html" -A "Mozilla/5.0 (Windows NT 6.1)"'%(n, n)
		print sCmd
		os.system(sCmd)
	#}
#}

def ParseIndexPage():
#{
	aryRet = []
	fOut = open('data.txt', 'w')
	for n in range(1, 205):
	#{
		f = open('%d.html'%(n))
		sData = f.read()
		f.close()
		
		#
# 		print sData
		aryTmp = sData.split('<strong>番号大全</strong>')
		sData = aryTmp[1]
		
		aryTmp = sData.split('<article class="excerpt">')
# 		print aryTmp
		for item in aryTmp:
		#{
			print '---------------------------------'
			try:
			#{
				aryTmp = item.split('" class="thumb"/')
				sThumnb = aryTmp[0].split('<img data-src="')[1]
				print sThumnb
				
				aryTmp = aryTmp[1].split('">')
				sPageURI = aryTmp[0].split('href="')[1]
				print sPageURI
				
				aryTmp = aryTmp[1].split('</a></h2>')
				sTitle = aryTmp[0]
# 				print sTitle
				sName = sTitle.split('番号')[0]
				sName = sName.replace('/', '_')
				print sName
				
 				aryTmp = item.split('<p class="note">')
 				sComm = aryTmp[1].split('</p>')[0].replace('\t', '')
#  				print sComm
 				
 				jsData = {
 					'thumnb': sThumnb,
 					'page': sPageURI,
 					'title': sTitle,
 					'name': sName,
 					'comm': sComm
 				}
 				fOut.write(json.dumps(jsData,ensure_ascii=False))
 				fOut.write('\n')
# 				fOut.write(sName + '|' + sThumnb + '|' + sPageURI + '|' + sComm + '\n')
				aryRet.append(jsData)
			#}
			except:
			#{
				print 'except: ' + item
			#}
		#}
	#}
	fOut.close()
	return aryRet
#}

def DownloadDetailPage(sActorName, sPageURI):
#{
	sCmd = 'curl -o "' + sActorName + '.html" "' + sPageURI + '" -A "Mozilla/5.0 (Windows NT 6.1)"'
	print sCmd
	os.system(sCmd)
#}

def DownloadThumnb(sActorName, sThumnbURI):
#{
	sCmd = 'curl -o "' + sActorName + '.jpg" "' + sThumnbURI + '" -A "Mozilla/5.0 (Windows NT 6.1)"'
	print sCmd
	os.system(sCmd)
#}

def DownloadPic(sActorName, sPicURI):
#{
	sCmd = 'curl -o "' + sActorName + '.jpg" --referer "http://www.99fanhao.com" "' + sPicURI + '" -A "Mozilla/5.0 (Windows NT 6.1)"'
	print sCmd
	os.system(sCmd)
#}

def ParseDetailPage():
#{
	# s3 = boto3.client('s3')

	# dynamodb
	db = boto3.resource('dynamodb')
	table = db.Table('avbus_programs')

	# mysql
	conn = mysql.connector.connect(
		user='avbus555',
		password='avbus555',
		host='avbus.c1dpvhbggytf.ap-southeast-1.rds.amazonaws.com',
		database='avbus'
	)

	cur = conn.cursor()

	# fOut = open('numberdata.txt', 'w')
	nCount = 0
	#<input type=hidden value=
	# sDir = '/Users/wanghao/OneDrive/wh/项目/some/Line55/detail/'
	sDir = '/app/Line55/detail/'
	#print 'CMediaSource::parse: ' + sDir
	files = os.listdir(sDir)
	for sFile in files:
	#{
		# sFile = 'Abigaile Johnson.html'
		if sFile == '.DS_Store':
			continue
		if os.path.isdir(sDir + sFile):
		#{
			continue
		#}
		print '--------------------------------------------------'
		print sDir + sFile
		sActor = sFile.replace('.html', '')
		sActor = sActor.split('个人资料')[0]
		sActor = sActor.split('资料')[0]
		sActor = sActor.replace('()', '')
		print '[' + sActor + ']'
		# continue
		f = open(sDir + sFile)
		sData = f.read()
		f.close()

		try:
		#{
			nCount += ParseDetailPage_One(sActor, sData, cur, table)
			conn.commit()

			print nCount
		#}
		except:
		#{
			print 'Except <------------>'
			conn.commit()
		#}
	#}
	conn.commit()

	cur.close()
	conn.close()

	# fOut.close()
#}

def ParseDetailPage_One(sActor, sData, msCur, table):
#{
	aryTmp = sData.split("<input type=hidden value='欢迎访问99番号网：www.99fanhao.com'>")

	# parse pic
	aryTmp = sData.split('<img src="http://www.99fanhao.com')
	if len(aryTmp) > 1:
	# {
		aryTmp = aryTmp[1].split('" />')
		sPicURI = 'http://www.99fanhao.com' + aryTmp[0]
		# DownloadPic(sActor, sPicURI)
	# }
	# parse table
	aryTmp = sData.split('<table class="fanhao_list_table">')
	sTable = aryTmp[1].split('</table>')[0]

	# line
	aryLines = sTable.split('</tr>')
	nCount = 0
	for sLine in aryLines:
	# {
		if sLine.find('</th>') > 0:
			continue
		# print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
		# print sLine
		sLine = sLine.replace('<tr>', '')
		sLine = sLine.replace('<td>', '')
		sLine = sLine.replace('</thead>', '')
		sLine = sLine.replace('<tbody>', '')

		aryFields = sLine.split('</td>')
		if len(aryFields) < 5:
			continue
		# print aryFields
		sNo = aryFields[0].replace('<td style="text-align: left">', '')
		sProgramName = aryFields[1].replace('<td style="text-align: left">', '')
		sProgramName = sProgramName.strip()
		sProgramName = sProgramName.replace('\r', '')
		sProgramName = sProgramName.replace('\n', '')
		sDur = aryFields[2].replace('<td style="text-align: left">', '')
		sDur = sDur.replace('分钟', '')
		nDur = int(sDur)
		sRelease = aryFields[3].replace('<td style="text-align: left">', '')
		sCompany = aryFields[4].replace('<td style="text-align: left">', '')

		nCount += 1
		print '    ->[%d] ' % (nCount) + sNo + '|' + sProgramName + '|%d' % (nDur) + '|' + sRelease + '|' + sCompany

		jsData = {
			'no': sNo,
			'name': sProgramName,
			'dur': nDur,
			'release': sRelease,
			'company': sCompany
		}
		# save to s3
		# sKey = sActor + '/' + sNo + '_' + sProgramName + '.json'
		# s3.put_object(Bucket='avline-data', Key=sKey, Body=json.dumps(jsData), ACL='public-read', ContentType='text/html')

		# save to mysql
		aryRelease = sRelease.split('-')
		nYear = 0
		nMonth = 0
		nDay = 0
		if len(aryRelease) == 3:
		# {
			nYear = int(aryRelease[0])
			nMonth = int(aryRelease[1])
			nDay = int(aryRelease[2])
		# }
		sSql = 'insert into programs(number, actor, name, dur, releaseYear, releaseMonth, releaseDay, company) values("' + sNo + '", "' + sActor + '", "' + sProgramName + '", %d, %d, %d, %d, ' % (nDur, nYear, nMonth, nDay) + '"' + sCompany + '")'
		print sSql
		msCur.execute(sSql)

		# save to dynamodb
		putItem2DynamoDB(sNo, sActor, sProgramName, sDur, nYear, nMonth, nDay, sCompany, table)
	#}
	return nCount
#}

def putItem2DynamoDB(sNumber, sActor, sProgramName, sDur, nYear, nMonth, nDay, sCompany, table):
#{
	table.put_item(Item={'no': sNumber, 'actor': sActor, 'name': sProgramName, 'dur': int(sDur), 'releaseYear': nYear, 'releaseMonth': nMonth, 'releaseDay': nDay, 'company': sCompany})
#}

#
# def ChangePicsACL():
# #{
# 	s3 = boto3.resource('s3')
# 	bucket = s3.Bucket('avline-data')
# 	for key in bucket.objects.all():
# 	#{
# 		if key.key.find('.jpg') >= 0:
# 		#{
# 		 	print key.key
# 			s3.Object('avline-data', key.key).put(ACL='public-read')
# 		#}
# 	#}
# #}

def UploadCoversToS3():
#{
	s3 = boto3.resource('s3')
	sDir = '/app/pics/'
	pics = os.listdir(sDir)
	for sFn in pics:
	#{
		if sFn.find('.jpg') < 0:
			continue
		print sDir + sFn
		s3.Object('avline-data', 'covers/' + sFn).put(Body=open(sDir + sFn, 'rb'), ACL='public-read')
	#}
#}

if __name__ == '__main__':
#{
	# step 1
# 	DownloadIndexPage()

	# step 2
	# aryActors = ParseIndexPage()
	# for actor in aryActors:
	# #{
	# 	DownloadDetailPage(actor['name'], actor['page'])
	# 	DownloadThumnb(actor['name'], actor['thumnb'])
	# #}

	# step 3
	# ParseDetailPage()

	# change pics acl
	#UploadCoversToS3()

	# write meta to dynamodb
	ParseDetailPage()

	# s3 = boto3.resource('s3')
	# # s3.Object(sBucket, sKey).put(ContentType='image/jpeg')
	# s3.Object(sBucket, sKey).Acl().put(ACL='public-read')

#}


