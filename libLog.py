#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import json
import time
import logging
from logging.handlers import TimedRotatingFileHandler

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
class CLog:
#{
  def __init__(self):
  #{
    self.m_bInited = False
    self.m_log = None
    self.m_sVer = '0'

    self.m_log_file_handler = None
  #}

  def Init(self, sLogFilename, sVer, sWhen='D', nInterval=1, nBackupCount=7):
  #{
    self.m_sVer = sVer
    #日志打印格式
    #log_fmt = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s'
    log_fmt = '%(asctime)s|%(levelname)s|%(message)s'
    formatter = logging.Formatter(log_fmt)

    #创建TimedRotatingFileHandler对象

    self.m_log_file_handler = TimedRotatingFileHandler(filename=sLogFilename, when=sWhen, interval=nInterval, backupCount=nBackupCount)

    self.m_log_file_handler.suffix = "%Y%m%d%H%M.log"
    #log_file_handler.extMatch = re.compile(r"^\d{4}\d{2}\d{2}\d{2}\d{2}.log$")

    self.m_log_file_handler.setFormatter(formatter)

    logging.basicConfig(level=logging.INFO)

    self.m_log = logging.getLogger()
    self.m_log.addHandler(self.m_log_file_handler)

    self.m_bInited = True
  #}

  def Close(self):
  #{
    if self.m_log_file_handler != None:
      self.m_log.removeHandler(self.m_log_file_handler)
    self.m_bInited = False
  #}

  def Info(self, sMsg):
  #{
    self.m_log.info(self.m_sVer + '|' + sMsg)
  #}

  def Warn(self, sMsg):
  #{
    self.m_log.warn(self.m_sVer + '|' + sMsg)
  #}

  def Err(self, sMsg):
  #{
    self.m_log.error(self.m_sVer + '|' + sMsg)
  #}
#}


def main():
#{
  log = CLog()
  log.Init("/Users/wanghao/OneDrive/DaBo/src/srv_libs/test.log", '1')

  #循环打印日志
  count = 0
  while count < 300:
    #log.error(log_content)
    log.Info('test|' + str(count))
    time.sleep(10)
    count = count + 1
#}

#-------------------------------------------------------#
if __name__ == '__main__':
  main()
  #test()

