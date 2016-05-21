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

from flask import Flask, render_template, request, Blueprint

#app = Flask( __name__ )
app = Blueprint( 'jw3', __name__, template_folder='templates', static_folder='static' )


@app.route( '/' )
def index():
    return render_template( 'indexme.html' )

from time import time
from queryAll import queryHuman
@app.route( '/SearchChensFriends', methods=["GET"] )
def chens():
    keyword = request.args.get( 'keyword', '' ) if request.method == "GET" else ''
    need_400 = request.args.get( 'db400', '' ) if request.method == "GET" else ''
    need_160 = request.args.get( 'db160', '' ) if request.method == "GET" else ''
    need_200 = request.args.get( 'db200', '' ) if request.method == "GET" else ''
    need_urp = request.args.get( 'dburp', '' ) if request.method == "GET" else ''
    need_eol = request.args.get( 'dbeol', '' ) if request.method == "GET" else ''
    need_ystu = request.args.get( 'dbystu', '' ) if request.method == "GET" else ''
    need_nstu = request.args.get( 'dbnstu', '' ) if request.method == "GET" else ''
    need_ku = map( lambda x: 1 if x else 0, [need_400, need_160, need_200, need_urp, need_eol, need_ystu, need_nstu] )
    btime = time()
    ineed1 = queryHuman( need_ku, keyword ) if keyword else []
    ineed2 = ['Elapsed time: %.2f s'%(time() - btime)] + ineed1
    return render_template( 'SearchMyFriends.html', ineed=ineed2 )

@app.route( '/wiki' )
def getwiki():
    return render_template( 'wiki.html' )

@app.route( '/bitbucket' )
def bitbucket_cp():
    return render_template( 'bitbucket.html' )

@app.route( '/login', methods=['GET', 'POST'] )
def login():
    #return "<script>alert('life')</script>"
    return render_template( 'touch.html' )
    return (request.form.get( 'user', 'you are interesting' ),
            request.form.get( 'pass', 'haha, you are crazy' )).__str__(), 9999

if __name__ == '__main__':
    #app.run( host="0.0.0.0", port=7777, debug=False )
    app.run( host="127.0.0.1", port=7777, debug=True )
