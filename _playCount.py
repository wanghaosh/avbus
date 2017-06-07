#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
import base64
import datetime
import traceback

# from cassandra.cluster import Cluster
# from cassandra.policies import DCAwareRoundRobinPolicy
sys.path.append('/app/srv_libs/')
# from libDBCassandra import CCassandra
# from libDBCassandra import Ccontents_content_base
from libMemC import CMemCached
from libSetting import CSetting
# from libLog import CLog

import boto3
import botocore
from botocore import response

# from _play_spec import CM3u8Spec
# g_M3u8Spec = CM3u8Spec()

##############################################################
def _getOneProgramPlayCount(sCmsCode):#, conn):
#{
  try:
  # {
    # 2016.11.25 add by wh [降低Cassandra负载] start
    mem = CMemCached()

    sKey = 'playcount_' + sCmsCode
    sKey = sKey.encode('utf-8')
    sRet = mem.Get(sKey)
    # sRet = None
    if sRet != '' and sRet != None:
    #{
      return int(sRet)
    #}

    nCount = _GetPlayCountFromS3(sCmsCode)

    # 2016.03.20 add by wh [使用S3代替Cassandra] start
    # # 2016.11.25 add by wh [降低Cassandra负载] end

    # # 2017.02.13 add by wh [启用内容trace表，降低cassandra负载] start
    # # conn.execute('use uss')
    # # sCQL = "select count(*) from playhistory where contentid='" + sCmsCode + "'"
    # conn.execute('use contents')
    # sCql = "select count(*) from trace where cmscode='" + sCmsCode + "' and act='playe'"
    # # 2017.02.13 add by wh [启用内容trace表，降低cassandra负载] end

    # datas = conn.execute(sCql)

    # for data in datas:
    # # {
    #   #print data
    #   # 2016.09.22 add by wh [应陈旭辉要求，播放数字乘以51] start
    #   # return data.count
    #   mem.Set(sKey, str(data.count * 51), 600)
    #   return data.count * 51
    #   # 2016.09.22 add by wh [应陈旭辉要求，播放数字乘以51] start
    # # }
    # nCount = nCount * 51
    mem.Set(sKey, str(nCount), 60)
    return nCount
    # 2016.03.20 add by wh [使用S3代替Cassandra] end
  # }
  except:
  # {
    #return -1
    info = sys.exc_info()
    print str(info) 
    return 0
  # }
  return 0
#}

def _GetPlayCountFromS3(sCmsCode):
  """
  此处的数据是由Lambda函数在日志上传到S3时分析日志写入S3的跟踪信息
  """
#{
  s3 = boto3.client('s3')

  sBucket = 'avk-trace-content'
  sKey = sCmsCode + '/playcount.info'

  try:
  #{
    response = s3.get_object(Bucket=sBucket, Key=sKey)
    rs = response['Body']

    sData = rs.read()
    
    jsData = json.loads(sData)
    return jsData['playcount']
  #}
  except:
  #{
    return 0
  #}
#}

def _playCount(sCmsCode, log):
#{
  # nCount = 0

  # cluster = Cluster(CSetting.aryCassandraCluster, load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='datacenter1'))
  # conn = cluster.connect()
  nCount = 0
  try:
  #{
    nCount = _getOneProgramPlayCount(sCmsCode)#, conn)
    # cluster.shutdown()
  #}
  except:
  #{
    # cluster.shutdown()
    log.Err('Except: ' + str(traceback.format_exc()))
  #}

  if nCount < 0:
  #{
    ret = {
      "result": "-ERR",
      "cmscode": sCmsCode,
      "count": 0
    }
    return json.dumps(ret, ensure_ascii=False)
  #}
  ret = {
    "result":"+OK",
    "cmscode":sCmsCode,
    "count": nCount
  }
  return json.dumps(ret, ensure_ascii=False)
#}

def _playCount_Mulit(sCmsCodes, log):
#{
  if sCmsCodes == None:
  #{
    ret = {
      "result":"-ERR",
      "data":"{}",
      "info":"cmscodes=None"
    }
    return json.dumps(ret, ensure_ascii=False)
  #}

  sCmsCodes = sCmsCodes.replace('[', '')
  sCmsCodes = sCmsCodes.replace(']', '')
  sCmsCodes = sCmsCodes.replace('"', '')
  aryCodes = sCmsCodes.split(',')
  #
  # cluster = Cluster(CSetting.aryCassandraCluster, load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='datacenter1'))
  # conn = cluster.connect()

  dictDatas = {}
  for sCode in aryCodes:
  #{
    nCount = 0
    try:
    #{
      # 2017.03.03 add by wh [CmsCode与RCode在一起] start
      aryCode = sCode.split('-')
      sCmsCode = aryCode[0]
      # 2017.03.03 add by wh [CmsCode与RCode在一起] end

      nCount = _getOneProgramPlayCount(sCmsCode)#, conn)
    #}
    except:
    #{
      log.Err('Except: ' + str(traceback.format_exc()))
    #}
    dictDatas[sCmsCode] = nCount
  #}
  # cluster.shutdown()

  ret = {
    "result":"+OK",
    "data":dictDatas
  }
  return json.dumps(ret, ensure_ascii=False)
#}

#-------------------------------------------------------#
if __name__ == '__main__':
#{
  #run()
  #notifyCMS_standalone()
  if len(sys.argv) <= 1:
  #{
    print 'unknown act code'
  #}
  else:
  #{
    sAct = sys.argv[1]
    if sAct == 'test':
    #{
      # sToken = sys.argv[2]
      sCmsCode = sys.argv[2]
      # print _playGetURL(sToken, sCmsCode, None)
      print _getOneProgramPlayCount(sCmsCode)
    #}
    else:
    #{
      print 'Act not support'
    #}
  #}
#}
