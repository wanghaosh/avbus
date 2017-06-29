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
from IProfile import _IProfile
from IR_a import _IR_a

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

@app.route('/api/license', methods=['GET'])
def IGetLicense():
#{
	sLicense = '用户协议\n'
	sLicense += '特别提示\n'
	sLicense += '福利书在此特别提醒您（用户）在成为用户之前，请认真阅读本《用户协议》（以下简称“协议”），确保您充分理解本协议中各条款。请您审慎阅读并选择接受或不接受本协议。除非您接受本协议所有条款，否则您无权使用本协议所涉服务。您的使用行为将视为对本协议的接受，并同意接受本协议各项条款的约束。\n'

	sLicense += '1）福利书是一个索引工具，仅提供查询影片信息的功能，并不提供影片内容（不提供播放，也不提供指向影片的链接）。\n'
	sLicense += '2）服务中所有的内容（文字、图片）均通过公开网络获取，为符合法律法规的要求，已采用技术手段对部分内容进行了过滤和隐藏。如因技术问题出现遗漏，请确认您所处的地域法律法规是否禁止此类内容，如果该内容是被法律法规所禁止的，请您中止访问并提交反馈帮助我们进行调整以符合法规要求。\n'
	sLicense += '3）如果您未满18岁或者您在您的居住管辖区内属于未成年人，请立即离开。\n'

	return sLicense
#}

@app.route('/api/search/hotwords', methods=['GET'])
def ISearchR():
	"""
	搜索的热词推荐
	:return:
	"""
#{
	return '{"result": "+OK", "data": ["里美", "麻生希", "Rio", "三上悠", "上原亚衣", "julia", "冲田杏梨", "吉泽明步", "大桥未久", "小川阿佐美"]}'
#}

@app.route('/api/r/a', methods=['GET'])
def IR_a():
#{
	return _IR_a(["47", "91", "121", "470", "576", "954", "1222", "1299", "1465", "1497", "1977", "2203"], g_log)
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
	sActorID = getParam(request, 'actorid', None)
	nPageIndex = int(getParam(request, 'pageindex', '0'))
	nPageSize = int(getParam(request, 'pagesize', '10'))
	return _IGetActorProgramList(sActor, sActorID, nPageIndex, nPageSize, g_log)
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
	nMaxCount = getParam(request, 'count', 10)

	return _ISearch(sToken, sActor, sProgramName, nMaxCount, g_log)
#}

@app.route('/api/profile', methods=['POST'])
def IProfile():
#{
	sToken = getParam(request, 'token', None)

	return _IProfile(sToken, g_log)
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
