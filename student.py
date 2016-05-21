#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    >  Filename : student.py
    >  Author   :
  donghouhe

    >  Date     : 15/09/05 - 19:02

'''
from jw import jw
from hashlib import md5
import sys

import requests

from optparse import OptionParser
parser = OptionParser( usage='python this.py --stuid 123 --pwd 321' )
parser.add_option("-s", "--stuid", dest="stuid",help="Student id")
parser.add_option("-p", "--pwd", dest="pwd",help="Password")
(options, args) = parser.parse_args()
stuid = options.stuid
pwd = options.pwd
if not (stuid and pwd):
	parser.parse_args(['-h'])
session = requests.Session()
loginurl =  'http://58.192.142.134:7777/pls/wwwbks/bks_login2.uniteLogin?stuid={}&pwd={}'.format( stuid, md5(pwd).hexdigest().upper() )
#print loginurl
s = session.get( loginurl )
if len( s.content ) < 100:
	print 'Login Failed!\nerror id or password or network'
	sys.exit(1)
s1 = session.get( 'http://58.192.142.134:7777/pls/wwwbks/bkscjcx.curscopre' ).content.decode('gbk').encode('utf-8')
s2 = session.get( 'http://58.192.142.134:7777/pls/wwwbks/bkscjcx.yxkc' ).content.decode('gbk').encode('utf-8')
jw( s1, s2 )
session.close()
