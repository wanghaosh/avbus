#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
import base64
import datetime
import traceback

sys.path.append('/app/srv_libs/')
from libDBCassandra import CCassandra
from libDBCassandra import Ccontents_content_base

from _play_spec import CM3u8Spec
g_M3u8Spec = CM3u8Spec()

##############################################################
def _playM3u8(sUrl, sBitrate, sType, sTicket, log):
#{
  if sTicket == '' or sTicket == 'null' or sTicket == None:
    return None

  cass = CCassandra()
  ccb = Ccontents_content_base(cass)

  it = None
  try:
  #{
    nItemCount = 0
    nRetryCount = 0
    while nItemCount <= 0 and nRetryCount < 5:
    #{
      it = ccb.FindWith_CmsCode(sUrl)

      nItemCount = len(it)
      nRetryCount += 1
    #}
    cass.Close()
  #}
  except:
  #{
    cass.Close()
    if log:
    #{
      log.Err('Except: ' + str(traceback.format_exc()))
    #}
    return None
  #}

  if it == None or len(it) <= 0:
  #{
    print 'Not Found Video [' + sUrl + ']'
    # cass.Close()
    # return 'Not Found Video [' + sUrl + ']'
    return None
  #}
  
  sData = '#EXTM3U\n'
  sData += '#EXT-X-VERSION:3\n'

  # 2016.10.08 add by wh [修正main m3u8未加路径的bug] start
  dateUrl = ''
  try:
  #{
    if it[0].has_key('info'):
    #{
      bi = it[0]['info'][0]
      if bi.has_key('dateUrl'):
        dateUrl = bi['dateUrl']
        dateUrl = '/' + bi['dateUrl']
      # if len(dateUrl.split('/')) < 4:
      #   dateUrl = dateUrl + '/'
      dateUrl = dateUrl + '/'
      dateUrl = dateUrl.replace('//', '/')
    #}
  #}
  except:
  #{
    print 'Get dateUrl Failed'
  #}
  # 2016.10.08 add by wh [修正main m3u8未加路径的bug] end

  if sType == 'index':
  #{
    nMinBitrate = 50 * 1024 * 1024
    aryM3u8 = []
    for brItem in it[0]['info']:
    #{
      # 不要纯音频,1080p,240p
      if brItem['audio-only'] != 0 or brItem['bitrate'] > 2000000 or brItem['bitrate'] < 500000:
        continue

      di = {}
      di['info'] = '#EXT-X-STREAM-INF:PROGRAM-ID=1,'\
             + 'BANDWIDTH=' + str(brItem['bitrate'])\
             + ',RESOLUTION=' + brItem['resolution']\
             + ',CODECS="' + brItem['codec'] + '"'\
             + '\n'

      di['data'] = 'media' + dateUrl + sUrl + '/' + str(brItem['bitrate']) + '/sub.m3u8?ticket=index\n'

      if brItem['bitrate'] < nMinBitrate and brItem['audio-only']==0:
        aryM3u8.insert(0, di)
        nMinBitrate = brItem['bitrate']
      else:  
        aryM3u8.append(di)
    #}
    for di in aryM3u8:
    #{
      print di
      sData += di['info']
      sData += di['data']
    #}
  #}
  elif sType == 'sub':
  #{
    sData = _makeSubM3u8(sUrl, sBitrate, it[0], sData)
  #}
  # cass.Close()
  return sData
#}

##############################################################
def _makeSubM3u8(sCmsCode, sBitrate, it, sData):
#{
  sData += '#EXT-X-TARGETDURATION:10\n'

  # 如果某些视频需要跳过片头
  nHeadSkipClips = g_M3u8Spec.GetHeadSkipDur(sCmsCode) / 10

  for brItem in it['info']:
  #{
    if str(brItem['bitrate']) == sBitrate:
    #{
      bMulitZip = brItem.has_key('zip')
      # 单一zip的旧格式
      fDur = float(it['dur'])

      nIndex = 0
      while fDur > 0:
      # {
        nIndex += 1

        if nHeadSkipClips <= 0:
        #{
          if fDur >= 10:
          # {
            sData += '#EXTINF:10.000,\n'
          # }
          else:
          # {
            sData += '#EXTINF:' + str(fDur) + ',\n'
          # }

          ########################
          if bMulitZip == True:
          #{
            sSeg = _getZipSegmentByIndex(nIndex, brItem['zip'])
            if sSeg == None:
              sData += 'NoFoundSeg.ts\n'
            else:
              sData += sSeg + '/' + str(nIndex) + '.ts\n'
          #}
          else:
          #{
            sData += str(nIndex) + '.ts\n'
          #}
        #}
        else:
        #{
          nHeadSkipClips -= 1
        #}
        fDur -= 10
      # }
      sData += '#EXT-X-ENDLIST\n'
    #}
  #}
  return sData
#}

##############################################################
def _getZipSegmentByIndex(nIndex, zipInfo):
#{
  for zk, zv in zipInfo.items():
  #{
    aryIndexs = zk.split('-')
    nStart = int(aryIndexs[0])
    nEnd = int(aryIndexs[1])
    if nIndex >= nStart and nIndex <= nEnd:
      return zk
  #}
  return None
#}

# #-------------------------------------------------------#
if __name__ == '__main__':
#{
  sCmsCode = 'CMMU299798'
  sTicket = 'public'
  # print _playM3u8(sCmsCode, 'all', 'index', sTicket, None)
  print _playM3u8(sCmsCode, '510200', 'sub', sTicket, None)
#   #run()
#   #notifyCMS_standalone()
#   if len(sys.argv) <= 1:
#   #{
#     print 'unknown act code'
#   #}
#   else:
#   #{
#     sAct = sys.argv[1]
#     if sAct == 'test':
#     #{
#       sToken = sys.argv[2]
#       sCmsCode = sys.argv[3]
#       print _playGetURL(sToken, sCmsCode, None)
#     #}
#     else:
#     #{
#       print 'Act not support'
#     #}
#   #}
# #}
