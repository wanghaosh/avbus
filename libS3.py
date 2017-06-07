#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import math
import json
import commands
#from cassandra.cluster import Cluster
import datetime
#import memcache
import time

import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from filechunkio import FileChunkIO

class CS3Bucket:
#{
  def __init__(self, sBucket, sRegion='us-east-2'):
  #{
    self.m_sRegion = sRegion
    self.m_sBucket = sBucket

    sAccessKey = 'AKIAJWXSUOUI2SVBAUVQ'
    sSecretKey = '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'

    conn = boto.s3.connect_to_region(region_name=self.m_sRegion,
                                     aws_access_key_id = sAccessKey,
                                     aws_secret_access_key = sSecretKey)

    #print conn.get_all_buckets()
    self.m_bucket = conn.get_bucket(sBucket)
  #}

  def Upload(self, sLocalFn, sKey, sPolicy=None):
  #{
    # try:
    # #{
    key = Key(self.m_bucket)
    key.key = sKey

    key.set_contents_from_filename(sLocalFn, policy=sPolicy)
    key.close()
    # #}
    # except:
    # #{
    #   return False
    # #}
    return True
  #}

  def Download(self, sS3Key, sLocalFn):
  #{
    #try:
    #{
    key = Key(self.m_bucket)
    key.key = sS3Key

    key.get_contents_to_filename(sLocalFn)
    key.close()
    #}
    #except:
    #{
    #  return False
    #}
    return True
  #}

  def List(self, sPrefix=''):
  #{
    aryRet = []
    ls = self.m_bucket.list(prefix = sPrefix)
    for item in ls:
    #{
      #print item.name
      aryRet.append(item.name.encode('utf-8'))
    #}
    return aryRet
  #}

  def Delete(self, sKey):
  #{
    print 'S3 Delete: [' + sKey + ']'
    self.m_bucket.delete_key(sKey)
  #}

  def Copy(self, sSrcKey, sDestKey):
  #{
    print 'S3 Copy: [' + sSrcKey + ' -> ' + sDestKey + ']'
    res = self.m_bucket.copy_key(new_key_name = sDestKey, src_bucket_name = self.m_sBucket, src_key_name = sSrcKey)
    return res.name.encode('utf-8')
  #}

  def Move(self, sSrcKey, sDestKey):
  #{
    res = self.Copy(sSrcKey, sDestKey)
    if res != None:
    #{
      self.Delete(sSrcKey)
    #}
  #}
  # def UploadMultipart(self, sLocalFn, sKey):
  # #{
  #   nSrcSize = os.stat(sLocalFn).st_size
  #   mp = self.m_bucket.initiate_multipart_upload(os.path.basename(sLocalFn))
  #
  #   # use a chunk size of 50MB
  #   chunk_size = 52428800
  #   chunk_count = int(math.ceil(nSrcSize / float(chunk_size)))
  #
  #   #
  #   for i in range(chunk_count):
  #   #{
  #     offset = chunk_size * i
  #     print '  chunk: ' + str(i) + ' / ' + str(offset)
  #     bytes = min(chunk_size, nSrcSize - offset)
  #     with FileChunkIO(sLocalFn, 'r', offset=offset,bytes=bytes) as fp:
  #       mp.upload_part_from_file(fp, part_num=i+1)
  #   #}
  #   mp.complete_upload()
  # #}
#}

def test():
#{
  sb = CS3Bucket(sBucket='dabo-media-src', sRegion='cn-north-1')
  #sb = CS3Bucket(sBucket='dabo-media-source', sRegion='ap-southeast-1')
  #sb.Upload('/Users/wanghao/Desktop/test.jpg', 'test/t.jpg')
  #sb.UploadMultipart('/Users/wanghao/Downloads/xampp-linux-x64-5.6.21-0-installer.run', 'test/xampp.run')
  #sb.Upload('/data/clips.py', 'clips.py')
  sb.Download('2016/09/07/VETL909560/400200/1-146.zip', '/data/test.zip')
#}

def t2():
#{
  sb = CS3Bucket(sBucket='dabo-media-src', sRegion='cn-north-1')
  print sb.List(sPrefix='tasks/ch_x/waitting4trans/')
  sb.Move('tasks/ch_x/waitting4trans/url.txt', 'tasks/ch_x/waitting4up2cdn/url.txt')
  #print sb.List('2016/09/13/')
#}

#-------------------------------------------------------#
if __name__ == '__main__':
#{
  sAct = sys.argv[1]
  if sAct == 'rm':
  #{
    sKey = sys.argv[2]
    sb = CS3Bucket('dabo-logs-sg', 'ap-southeast-1')
    aryList = sb.List(sPrefix= sKey)
    for item in aryList:
    #{
      print item
      sb.Delete(item)
    #}
  #}
  elif sAct == 'ls':
  #{
    sBucket = sys.argv[2]
    sPrefix = sys.argv[3]

    sb = CS3Bucket(sBucket, 'us-east-2')
    aryList = sb.List(sPrefix)
    for item in aryList:
    #{
      print item
    #}
  #}
#}
  #test()
  # t2()
  #run()
  #upload2S3('213925')
  #print 'notify'
  #notify('1', 'a', 'A', 0)

  # get queue
  #notify('2', 'hahaha', 'k', 4)
  #time.sleep(5)
  #test()

