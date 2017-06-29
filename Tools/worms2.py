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
	#}

	def GetAllPage(self):
	#{
		for nPageName in range(86, 513):
		#{
			while nPageIndex >= 0:
			#{
				if nPageIndex == 0:
				#{
					nPageIndex = self.GetOnePage('%d.html'%(nPageName))
				#}
				else:
				#{
					nPageIndex = self.GetOnePage('%d-%d.html' % (nPageName, nPageIndex))
				#}
			#}
		#}
	#}

	def GetOnePage(self, sPageName):
	#{
		print sPageName
	#}
#}


if __name__ == '__main__':
#{
	site = C1sdy()
	site.GetAllPage()
#}


