#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    >  Filename : loginwooyun.py
    >  Author   :
 ____     __
/\  _`\  /\ \
\ \ \/\_\\ \ \___      __    ___
 \ \ \/_/_\ \  _ `\  /'__`\/' _ `\
  \ \ \L\ \\ \ \ \ \/\  __//\ \/\ \
   \ \____/ \ \_\ \_\ \____\ \_\ \_\
    \/___/   \/_/\/_/\/____/\/_/\/_/

    >  Date     : 15/04/18 - 17:46

'''

import json
import re
import md5
import requests
proxies={}#{'http': 'http://127.0.0.1:8080'}
host = 'zone.wooyun.org'
headers={ "Host": host,
          "Origin": "http://"+host,
          "User-Agent": "Mozilla/5.0  AppleWebKit/537.36 (KHTML, like Gecko) asibutian of 360",
          }

def getsession():
	session = requests.Session()
	return session

def getcaptcha( session ):
    vcode = session.get( 'http://' + host + '/captcha.php', headers=headers, proxies=proxies, timeout=10)
    return session, vcode.content

def gettoken():
    session = getsession()
    tokenhtml = session.get( 'http://' + host + '/login', headers=headers, proxies=proxies, timeout=10).text
    token = re.search("loginToken=\'(.*?)\'", tokenhtml).group(1)
    return session, token

def getusers():
	with open(u'wa.txt') as usersfile:
		return [_.strip() for _ in usersfile]
def md5fy( src ):
    m = md5.new()
    m.update(src)
    return m.hexdigest()

def gologin( session2, token, yzm, username, password ):
    pwd = md5fy(md5fy( username + md5fy(password)) + yzm)
    loginsio = session2.post('http://' + host + '/index.php?do=login&act=ajax',
                      data = {'token': token,
                     'user': username,
                     'pwd': pwd,
                     'captcha': yzm
                     },
                     headers=headers, proxies=proxies, timeout=10)
    return len(json.loads(loginsio.text)['msg']) < 37#len(u"登录失败,请检查邮箱或密码")
