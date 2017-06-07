#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
# import base64
# import datetime
import traceback

# from cassandra.cluster import Cluster
# from cassandra.policies import DCAwareRoundRobinPolicy
sys.path.append('/app/srv_libs/')
from libDBCassandra import CCassandra
from libDBCassandra import Ccontents_content_base
# from libMemC import CMemCached
from libSetting import CSetting
# from libLog import CLog

# from _play_spec import CM3u8Spec
# g_M3u8Spec = CM3u8Spec()

# 2016.08.26 add by wh [support mp4 format/mulit media format] start
def _makeURL_mp4(item):
#{
    rates = []
    for bi in item['info']:
    # {
        # print bi
        lSize = 0
        if bi.has_key('size'):
            lSize = bi['size']
        # 2016.08.16 add by chen.yuxiang [修改CDN存放路径(每日一目录)] start
        # dateUrl = ''
        # if bi.has_key('dateUrl'):
        #   dateUrl = bi['dateUrl']
        # 2016.08.16 add by chen.yuxiang [修改CDN存放路径(每日一目录)] end

        sPath = ''
        if bi.has_key('path'):
            sPath = bi['path']
        bid = {
            'name': _getNameFromResolution(bi['resolution']),
            'rate': bi['bitrate'],
            'size': lSize,
            'uri': CSetting.sCDNBase + sPath,
        }
        rates.append(bid)
    # }
    return rates
#}

def _makeURL_hls(item, sVideoCode):
#{
    rates = []
    for bi in item['info']:
    # {
        # print bi
        # 暂时不提供音频码率
        if bi['audio-only'] != 0:
            continue

        ######
        lSize = 0
        if bi.has_key('size'):
            lSize = bi['size']

        # 2016.08.16 add by chen.yuxiang [修改CDN存放路径(每日一目录)] start
        dateUrl = ''
        if bi.has_key('dateUrl'):
            dateUrl = bi['dateUrl']
            if len(dateUrl.split('/')) < 4:
                dateUrl = dateUrl + '/'

        # 2016.08.16 add by chen.yuxiang [修改CDN存放路径(每日一目录)] end
        print bi
        bid = {
            'name': _getNameFromResolution(bi['resolution']),
            'rate': bi['bitrate'],
            'size': lSize,
            'uri': CSetting.sCDNBase + dateUrl + sVideoCode + '/' + str(bi['bitrate']) + '/sub.m3u8',
            'urim': CSetting.sCDNBase + dateUrl + sVideoCode + '/main.m3u8?bitrate=' + str(bi['bitrate'])
        }
        rates.append(bid)
    # }
    return rates
#}
# 2016.08.26 add by wh [support mp4 format/mulit media format] end

# 2016.07.12 add by wh [提供批量获取播放url功能] start
def _getOneProgramURL(sCode, ccb, log):
#{
    try:
    #{
        items = None
        nItemCount = 0
        nRetryCount = 0
        while nItemCount <= 0 and nRetryCount < 5:
        #{
            items = ccb.FindWith_CmsCode(sCode)
            nItemCount = len(items)
            nRetryCount += 1
        #}
        # 2016.07.19 add by wang.hao [不存在的节目crash] start
        if len(items) <= 0:
        #{
            print 'Not Found : ' + sCode
            ret = {
                "result": "+OK",
                "data": ""
            }
            return json.dumps(ret, ensure_ascii=False)
        #}
        # 2016.07.19 add by wang.hao [不存在的节目crash] end
        item = items[0]
        #sVideoCode = item['videocode']
        # 将cmscode当作videocode使用
        #sVideoCode = item['cmscode']
        rates = []
        # 2016.08.26 add by wh [support mp4 format/mulit media format] start
        print item
        sType = 'hls'
        if item.has_key('type'):
            sType = item['type']
        if sType == 'mp4':
        #{
            print 'make url mp4'
            rates = _makeURL_mp4(item)
        #}
        else:
        #{
            print 'make url hls'
            sVideoCode = item['cmscode']
            rates = _makeURL_hls(item, sVideoCode)
        #}

        retData = {
            "ver":1,
            "ticket":"public",
            "length":item["dur"],
            "rates":rates
        }
        return retData
    #}
    except:
    #{
        info = sys.exc_info()
        print info

        retData = {
            "ver":1,
            "ticket":"public",
            "length":0,
            "rates":{}
        }
        return retData
    #}
#}

def _playGetURL_Mulit(sToken, sCodes, log):
#{
    cass = CCassandra()
    ccb = Ccontents_content_base(cass)

    ret = {"result": "-ERR", "msg": "except"}
    try:
    #{
        sCodes = sCodes.replace('[', '')
        sCodes = sCodes.replace(']', '')
        sCodes = sCodes.replace('"', '')
        aryCodes = sCodes.split(',')

        #
        dictDatas = {}
        for sCode in aryCodes:
        #{
            # 2017.03.03 add by wh [CmsCode与RCode在一起] start
            aryCode = sCode.split('-')
            sCmsCode = aryCode[0]
            # 2017.03.03 add by wh [CmsCode与RCode在一起] end

            dictDatas[sCmsCode] = _getOneProgramURL(sCmsCode, ccb, log)
        #}

        cass.Close()
        ret = {
            "result":"+OK",
            "data":dictDatas
        }
    #}
    except:
    #{
        cass.Close()
        log.Err('Except: ' + str(traceback.format_exc()))
    #}
    return json.dumps(ret, ensure_ascii=False)
#}

# 2016.07.12 add by wh [提供批量获取播放url功能] end

##############################################################
def _playGetURL(sToken, sCode, log):
#{
    cass = CCassandra()
    ccb = Ccontents_content_base(cass)

    ret = {"result": "-ERR", "msg": "except"}
    try:
    #{
        retData = _getOneProgramURL(sCode, ccb, log)

        ret = {
            "result":"+OK",
            "data":retData
        }
        cass.Close()
    #}
    except:
    #{
        cass.Close()
        log.Err('Except: ' + str(traceback.format_exc()))
    #}
    return json.dumps(ret, ensure_ascii=False)
#}

def _getNameFromResolution(sResolution):
#{
    if sResolution == '1920x1080':
    #{
        return '1080P'
    #}
    elif sResolution == '1280x720':
    #{
        return '720P'
    #}
    elif sResolution == '720x480':
    #{
        return '480P'
    #}
    elif sResolution == '480x270':
    #{
        return '270P'
    #}
    elif sResolution == '320x240':
    #{
        return '240P'
    #}
    elif sResolution == '':
    #{
        return 'Audio'
    #}
    else:
    #{
        return 'unknown'
    #}
#}


# #-------------------------------------------------------#
# if __name__ == '__main__':
# #{
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
