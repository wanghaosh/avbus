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
			nPageIndex = 0
			while nPageIndex >= 0:
			#{
				bRetry = False
				while bRetry:
				#{
					if nPageIndex == 0:
					#{
						try:
						#{
							nPageIndex = self.GetOnePage('%d.html'%(nPageName))
						#}
						except:
						#{
							bRetry = True
						#}
					#}
					else:
					#{
						try:
						#{
							nPageIndex = self.GetOnePage('%d-%d.html' % (nPageName, nPageIndex))
						#}
						except:
						#{
							bRetry = True
						#}
					#}
				#}
			#}
			# break
		#}
		sData = json.dumps(self.m_dictActors, ensure_ascii=False)
		f = open('data_1sdy.json', 'w')
		f.write(sData)
		f.close()
	#}

	def GetOnePage(self, sPageName):
	#{
		print '-------------------------------'
		sUri = self.m_sBaseURI + sPageName
		print sUri
		sData = CHttp.HttpGet(sUri)
		# print sData
		sActor = sData.split('<title>')[1].split('所有作品番号')[0]
		# print sActor
		sPic = sData.split('.html"><img src="')[1].split('">')[0]
		# print '    -> ' + sPic

		sDetail = sData.split('简介</a>')[1].split('</div>')[0].replace('<br />', '\n').replace('<div class="u">', '').replace('</br>', '')
		# print sDetail

		self.AddActor(sActor, sPic, sDetail)

		aryProgramsTmp = sData.split('<div class="showPlay">')[1].split('<a href="')#.split('.html" target="_blank"><img src="')
		for sTmp in aryProgramsTmp:
		#{
			aryTmp = sTmp.split('" target="_blank"><img src="')
			if len(aryTmp) <= 1:
				continue
			sDetailPageUri = 'http://www.1sdy.com' + aryTmp[0]

			sOneProgram = aryTmp[1].split('"></a>')[0]
			aryTmp = sOneProgram.split('" alt="')
			sCoverPic = aryTmp[0]
			sNo = aryTmp[1].split(' ')[1]
			# print '    -> [' + sNo + '] ' + sDetailPageUri + ' / ' + sCoverPic
			# print '    -> ' + sNo

			# self.AddProgram(sActor, , sCoverPic, sNo, )
			self.GetProgramDetailPage(sDetailPageUri, sActor, sNo, sCoverPic)
		#}
		sTmp = sData.split('页次:')[1].split('页')[0]
		nCurPage = int(sTmp.split('/')[0])
		nTotalPage = int(sTmp.split('/')[1])
		print '[%d / %d]'%(nCurPage, nTotalPage)
		if nCurPage >= nTotalPage:
			return -1
		return nCurPage + 1
	#}

	def GetProgramDetailPage(self, sUri, sActor, sNo, sCoverPic):
	#{
		sData = CHttp.HttpGet(sUri)
		sData = sData.replace('\r', '').replace('\n', '').replace('<br>', '').replace('<p>', '')
		aryTmp = sData.split('<li class="small">')
		# for sTmp in aryTmp:
		# #{
		# 	print sTmp
		# #}
		sDT = aryTmp[3].replace('</li>', '')
		sName = aryTmp[7].replace('</li>', '')#.replace('\n', '')
		sInfo = sData.split('<div class="showInfo">')[1].split('</div>')[0]

		self.AddProgram(sActor, sName.strip(' '), sNo, sCoverPic, sInfo.strip(' '), sDT.strip(' '))
	#}

	def AddActor(self, sActor, sActorPic, sDetail):
	#{
		print sActor + ' : ' + sActorPic
		# print '  -> ' + sDetail
		if self.m_dictActors.has_key(sActor) is False:
		#{
			self.m_dictActors[sActor] = {}
		#}
		self.m_dictActors[sActor]['pic'] = sActorPic
		self.m_dictActors[sActor]['detail'] = sDetail
		if self.m_dictActors[sActor].has_key('programs') is False:
		#{
			self.m_dictActors[sActor]['programs'] = []
		#}
	#}

	def AddProgram(self, sActor, sProgramName, sProgramNo, sProgramCover, sProgramDetail, sDT):
	#{
		print '  -> [' + sProgramNo + '] ' + sDT + ' / ' + sProgramName
		# print '  -> [' + sProgramNo + '] ' + sProgramName# + ' / ' + sProgramDetail
		dictProgram = {
				'name': sProgramName.strip(' '),
				'no': sProgramNo.strip(' '),
				'cover': sProgramCover.strip(' '),
				'detail': sProgramDetail.strip(' '),
				'dt': sDT.strip(' ')
			}

		self.m_dictActors[sActor]['programs'].append(dictProgram)

		# download program cover
		sCmd = 'curl -o "' + sActor + '_' + sProgramNo + '.jpg" --referer "http://www.1sdy.com" "' + sProgramCover + '" -A "Mozilla/5.0 (Windows NT 6.1)"'
		print sCmd
		os.system(sCmd)

		f = open(sActor + '_' + sProgramNo + '.json', 'w')
		f.write(json.dumps(dictProgram, ensure_ascii=False))
		f.close()
	#}
#}


if __name__ == '__main__':
#{
	site = C1sdy()
	site.GetAllPage()
#}


