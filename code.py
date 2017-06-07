#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
push code to s3://avline-app/srv_api/
"""

import sys
import os

#-------------------------------------------------------#
if __name__ == '__main__':
#{
	sAct = sys.argv[1]
	if sAct == 'push':
	#{
		sCmd = 'aws s3 sync . s3://avline-app/srv_api/'
		print sCmd
		os.system(sCmd)
	#}
	elif sAct == 'pull':
	#{
		sCmd = 'aws s3 sync s3://avline-app/srv_api/ .'
		print sCmd
		os.system(sCmd)
	#}
	else:
	#{
		print 'unknown act code'
	#}
#}
