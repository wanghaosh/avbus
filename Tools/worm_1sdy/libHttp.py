#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wang.hao'

import urllib2
import urllib

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

