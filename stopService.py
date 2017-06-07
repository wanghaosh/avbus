#!/usr/bin/python

import os
import sys

def killService(sName):
#{
  sCmd = 'ps aux | grep ' + sName
  print sCmd
  ret_text_list = os.popen(sCmd)
  #print ret_text_list
  pid_list = []
  for line in ret_text_list:
  #{
    if line.find('grep') > 0 or line.find('stopService.py') > 0:
      continue
    #print line
    pid_list.append(line)
    cmd_list = line.split()
    pid_num = cmd_list[1]
    #print pid_num
    sCmd = 'kill -9 ' + pid_num
    #print sCmd
    os.system(sCmd)
  #}
#}

if __name__ == '__main__':
#{
  if len(sys.argv) <= 1:
  #{
    print 'need a service name(keyword)'
    exit(0)
  #}
  sName = sys.argv[1]
  killService(sName)
#}
