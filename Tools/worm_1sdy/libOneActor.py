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

# import boto
import boto3
# import botocore
import traceback
from libHttp import CHttp

class COneActor:
#{
	def __init__(self, nFirstPageIndex, aryMysql, s3, sLocalDataRootDir):
	#{
		self.m_sLocalDataRootDir = sLocalDataRootDir

		self.m_sActorDir = sLocalDataRootDir

		self.m_sBaseURI = 'http://www.1sdy.com/topiclist/'
		self.m_nFirstPageIndex = nFirstPageIndex

		self.m_sActorName = ''
		self.m_sActorPicUri = ''
		self.m_sActorInfo = ''
		self.m_aryPrograms = []

		self.m_aryMySQL = aryMysql
		self.m_s3 = s3
	#}

	def GetAndParse(self):
	#{
		nPageIndex = 0
		while nPageIndex >= 0:
		#{
			if nPageIndex == 0:
			#{
				sUri = '%d.html'%(self.m_nFirstPageIndex)
			#}
			else:
			#{
				sUri = '%d-%d.html' % (self.m_nFirstPageIndex, nPageIndex)
			#}
			# print sUri
			bRetryCount = 5
			nPageIndex = -1
			while bRetryCount > 0:
			# {
				try:
				# {
					nPageIndex = self._OnePage(sUri)
					print 'NextPage [%d]'%(nPageIndex)
					break
				# }
				except:
				# {
					info = sys.exc_info()
					print str(info)

					print traceback.format_exc()

					print 'Except[%d]: '%(bRetryCount) + sUri
					bRetryCount -= 1
				# }
			#}
		#}
	#}

	def _downloadPageFile(self, sUri, sPageName):
	#{
		sCmd = 'curl -o "' + self.m_sLocalDataRootDir + sPageName + '" --referer "http://www.1sdy.com" "' + sUri + '" -A "Mozilla/5.0 (Windows NT 6.1)"'
		print sCmd
		os.system(sCmd)
	#}

	def _parseActorBaseInfo(self, sData):
	#{
		self.m_sActorName = sData.split('<title>')[1].split('所有作品番号')[0].strip()
		self.m_sActorPicUri = sData.split('.html"><img src="')[1].split('">')[0].strip()
		self.m_sActorInfo = sData.split('简介</a>')[1].split('</div>')[0].replace('<br />', '\n').replace('<div class="u">', '').replace('</br>', '').strip()

		print self.m_sActorName + ' : ' + self.m_sActorPicUri
	#}

	def _parseProgramInfo(self, sData, nActorID, sActorName):
	#{
		aryProgramsTmp = sData.split('<div class="showPlay">')[1].split('<a href="')  # .split('.html" target="_blank"><img src="')
		for sTmp in aryProgramsTmp:
		# {
			aryTmp = sTmp.split('" target="_blank"><img src="')
			if len(aryTmp) <= 1:
				continue
			sDetailPageUri = 'http://www.1sdy.com' + aryTmp[0]

			sOneProgram = aryTmp[1].split('"></a>')[0]
			aryTmp = sOneProgram.split('" alt="')
			sCoverPic = aryTmp[0]
			sNo = aryTmp[1].split(' ')[1]

			self.GetProgramDetailPage(sDetailPageUri, nActorID, sActorName, sNo, sCoverPic)
		# }
	#}

	def _OnePage(self, sPageName):
	#{
		print ' '
		print ' '
		print '-------------------------------'
		sUri = self.m_sBaseURI + sPageName
		print sUri

		#
		sData = CHttp.HttpGet(sUri)

		self._parseActorBaseInfo(sData)
		# return -1

		nActorID = self._addActor2MySQL(self.m_sActorName, self.m_sActorPicUri, self.m_sActorInfo)

		self._parseProgramInfo(sData, nActorID, self.m_sActorName)

		sTmp = sData.split('页次:')[1].split('页')[0]
		nCurPage = int(sTmp.split('/')[0])
		nTotalPage = int(sTmp.split('/')[1])
		print '[%d / %d]'%(nCurPage, nTotalPage)
		if nCurPage >= nTotalPage:
			return -1
		return nCurPage + 1
	#}

	def GetProgramDetailPage(self, sUri, nActorID, sActor, sNo, sCoverPic):
	#{
		sData = CHttp.HttpGet(sUri)
		sData = sData.replace('\r', '').replace('\n', '').replace('<br>', '').replace('<p>', '')
		aryTmp = sData.split('<li class="small">')

		# sDT = aryTmp[3].replace('</li>', '').strip(' ')
		sDT = sData.split('发片日期是')[1][0:10]
		sName = aryTmp[7].replace('</li>', '').replace('别名：', '').strip(' ')#.replace('\n', '')
		sInfo = sData.split('<div class="showInfo">')[1].split('</div>')[0].strip(' ')
		nDur = 0
		try:
		#{
			nDur = int(sData.split('时长')[1].split('分钟')[0])
		#}
		except:
		#{
			print '    except: nDur'
		#}

		self.AddProgram(nActorID, sActor, sName, sNo, sCoverPic, sInfo, sDT, nDur)
	#}

	def _addActor2MySQL(self, sActor, sActorPic, sDetail):
	#{
		conn = self.m_aryMySQL[0]
		cur = self.m_aryMySQL[1]

		# 查询数据库中是否有同名演员（有，补充信息&获取id；无，新增记录获得id）
		sSql = 'select id from actors where name="' + sActor + '" and status=1'
		print sSql
		cur.execute(sSql)
		res = cur.fetchall()
		nID = 0
		for r in res:
		#{
			nID = r[0]
			break
		#}

		if nID > 0:
		#{
			sSql = 'update actors set detail="' + sDetail + '" where id=' + str(nID)
			print sSql
			cur.execute(sSql)
			conn.commit()
		#}
		else:
		#{
			# 数据库中没有同名演员
			sSql = 'insert into actors(name, alias, detail, cover_pic, status, program_count, src_site) values("' + sActor + '", "-", "' + sDetail + '", "' + sActorPic + '", 1, 0, "www.1sdy.com")'
			print sSql
			cur.execute(sSql)
			conn.commit()

			cur.execute('select @@IDENTITY')
			res = cur.fetchall()
			for r in res:
			#{
				nID = r[0]
				break
			#}
		#}

		print '    -> ID in MYSQL = %d'%(nID)

		self.m_sActorDir = self.m_sLocalDataRootDir + str(nID) + '_' + sActor + '/'
		if os.path.exists(self.m_sActorDir) is False:
		#{
			os.mkdir(self.m_sActorDir)
		#}

		# 下载人物图&上传到S3
		sLocalFn = self.m_sActorDir + '%d.jpg'%(nID)

		sCmd = 'curl -o "' + sLocalFn + '" --referer "http://www.1sdy.com" "' + sActorPic + '" -A "Mozilla/5.0 (Windows NT 6.1)"'
		print '    -> ' + sCmd
		os.system(sCmd)

		self.m_s3.Object('avbus-data', 'covers/%d.jpg' % (nID)).put(Body=open(sLocalFn, 'rb'), ACL='public-read')

		return nID
	#}

	def AddProgram(self, nActorID, sActorName, sProgramName, sProgramNo, sProgramCover, sProgramDetail, sDT, nDur):
	#{
		conn = self.m_aryMySQL[0]
		cur = self.m_aryMySQL[1]

		print '      -> [' + sProgramNo + '] ' + sDT + ' / ' + str(nDur) + '分钟 / ' + sProgramName
		dictProgram = {
				'name': sProgramName.strip(' '),
				'no': sProgramNo.strip(' '),
				'cover': sProgramCover.strip(' '),
				'detail': sProgramDetail.strip(' '),
				'dt': sDT.strip(' '),
				'dur': nDur
			}

		self.m_aryPrograms.append(dictProgram)

		# download program cover
		sCmd = 'curl -o "' + self.m_sActorDir + sProgramNo + '.jpg" --referer "http://www.1sdy.com" "' + sProgramCover + '" -A "Mozilla/5.0 (Windows NT 6.1)"'
		print '        -> ' + sCmd
		os.system(sCmd)

		self.m_s3.Object('avbus-data', 'covers/%d/'%(nActorID) + sProgramNo + '.jpg').put(Body=open(self.m_sActorDir + sProgramNo + '.jpg', 'rb'), ACL='public-read')

		# add to mysql
		aryDT = sDT.split('-')
		sSql = 'insert into programs(number, actor_id, actor, name, dur, releaseYear, releaseMonth, releaseDay, company, online, cover) values("'\
			   + sProgramNo + '", ' + str(nActorID) + ', "' + sActorName + '", "' + sProgramName + '", ' + str(nDur) + ', ' + aryDT[0] + ', ' + aryDT[1] + ', ' + aryDT[2] + ', "-", 1, "covers/%d/'%(nActorID) + sProgramNo + '.jpg")'
		print sSql
		cur.execute(sSql)
		conn.commit()
	#}
#}
#
# if __name__ == '__main__':
# #{
# 	site = C1sdy()
# 	site.GetAllPage()
# #}


