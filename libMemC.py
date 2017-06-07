#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import math
import json
import commands
##from cassandra.cluster import Cluster
import datetime
import memcache
import time

# from elasticsearch_dsl import DocType, String, Boolean
# from elasticsearch_dsl.connections import connections
# from libSetting import CSetting
# from requests_aws4auth import AWS4Auth

# from libSetting import CSetting

class CMemCached:
#{
  def __init__(self, sEndPoint = None):
  #{
    sEndPoint = 'avbus.b7enf8.0001.apse1.cache.amazonaws.com:11211'
    # if sEndPoint is None:
    # #{
    #   sEndPoint = CSetting.aryMemcachedCluster[0] + ':11211'
    # #}
    self.m_mem = memcache.Client([sEndPoint], debug=True)
    #value = mem.get('searchHotwords')
    #return value
  #}

  def Set(self, sKey, sValue, nExpire=0):
    """
    设置缓存

    Parameters:
      sKey: 键值
      sValue: 数据
      nExpire: 过期时间（秒）
    """
  #{
    return self.m_mem.set(sKey, sValue, nExpire)
  #}

  def Get(self, sKey):
  #{
    return self.m_mem.get(sKey)
  #}
#}

def test():
#{
  mem = CMemCached()
  #print mem.Set('test', 'hahaha')
  sKey = 'sub.m3u8_KIRA234944_400200'
  print mem.Get(sKey)
#}

#-------------------------------------------------------#
if __name__ == '__main__':
#{
  # test()
  sAct = sys.argv[1]
  if sAct == 'get':
  #{
    # sM = sys.argv[2]
    # sEndPoint = CSetting.aryMemcachedCluster[0]

    # if sM == 'r':
    #   sEndPoint = 'avk-greatr.htogla.0001.apse1.cache.amazonaws.com'

    # sKey = sys.argv[3]
    # sKey = sKey.encode('utf-8')
    # mem = CMemCached(sEndPoint)
    # print mem.Get(sKey)
    print 'get'
  #}
#}
  #run()
  #upload2S3('213925')
  #print 'notify'
  #notify('1', 'a', 'A', 0)

  # get queue
  #notify('2', 'hahaha', 'k', 4)
  #time.sleep(5)
  #test()

