#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
avbus555 web api service
"""

import json
# import base64
# import datetime
# import time
# import urllib2
# import urllib
import sys

from gevent import monkey
# from gevent.pywsgi import WSGIServer
monkey.patch_all()

# import mysql.connector
# from Crypto.Cipher import AES
# from binascii import b2a_hex, a2b_hex
# import zlib
#
# from libMemC import CMemCached
from libLog import CLog

# from libUser import CUser

from IGetActorList import _IGetActorList
from IGetActorProgramList import _IGetActorProgramList
from IGetNo import _IGetNo
from IGetYearsProgramList import _IGetYearsProgramList
from ISearch import _ISearch

################################
from flask import Flask
from flask import request

app = Flask(__name__)

g_log = CLog()
g_log.Init('/logs/avbus_api.log', '1')

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
def getParam(request, sParamName, sDefaultValue):
	"""
	get parameter from request
	"""
#{
	sParamValue = 'null'
	try:
	#{
		if request.method == 'GET':
		#{
			sParamValue = request.args.get(sParamName, sDefaultValue)
		#}
		elif request.method == 'POST':
		#{
			sParamValue = request.form[sParamName]
			if sParamValue == '' or sParamValue is None:
			#{
				sParamValue = sDefaultValue
			#}
		#}
	#}
	except:
	#{
		return sDefaultValue
	#}
	return sParamValue
#}

@app.route('/api/getactorlist', methods=['GET'])
def IGetActorList():
	"""
	interface: get actor list(full)
	"""
#{
	nPageIndex = int(getParam(request, 'pageindex', '0'))
	nPageSize = int(getParam(request, 'pagesize', '10'))
	return _IGetActorList(nPageIndex, nPageSize, g_log)
#}

@app.route('/api/getactorprogramlist', methods=['POST'])
def IGetActorProgramList():
	"""
	interface: get one actor's program list
	param:
		actor: actor name
	"""
#{
	sActor = getParam(request, 'actor', None)
	return _IGetActorProgramList(sActor, g_log)
#}


@app.route('/api/getno', methods=['POST'])
def IGetNo():
	"""
	interface: get one program's number(fanhao)
	param:
		token: user token, {"uid":"xxxx", "dt": "yyyymmddHHMMSS", "debug":true}
		id: program's id(database primary key)
	"""
#{
	sToken = getParam(request, 'token', None)
	sID = getParam(request, 'id', None)
	return _IGetNo(sToken, sID, g_log)
#}

@app.route('/api/<sYear>/getyearsprogramlist', methods=['POST'])
def IGetYearsProgramList(sYear):
#{
	sToken = getParam(request, 'token', None)
	nPageIndex = int(getParam(request, 'pageindex', '0'))
	nPageSize = int(getParam(request, 'pagesize', '10'))
	return _IGetYearsProgramList(sToken, int(sYear), nPageIndex, nPageSize, g_log)
#}

@app.route('/api/search', methods=['POST'])
def ISearch():
#{
	sToken = getParam(request, 'token', None)
	sActor = getParam(request, 'actor', None)
	sProgramName = getParam(request, 'program', None)

	return _ISearch(sToken, sActor, sProgramName)
#}

#-------------------------------------------------------#
if __name__ == '__main__':
#{
	sAct = sys.argv[1]
	if sAct == 'run':
	#{
		app.run(host='0.0.0.0', port=5001)
	#}
	else:
	#{
		print 'unknown act code'
	#}
#}
