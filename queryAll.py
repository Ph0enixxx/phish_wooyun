#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    >  Filename : queryAll.py
    >  Author   : donghouhe

    >  Date     : 15/06/06 - 14:03

'''
def queryHuman( selectors, keyword ):
    return
'''
from itertools import compress

def queryHuman( selectors, keyword ):
    #return ['测试中文olarry', 'page']
    resultInfo = []
    # 400, 160, 200, njutcm_urp, njutcm_eol, yangda_stu, njutcm_stu
    for datafile in compress( ['/Users/chencgbv/Downloads/Degree401.csv',
                               '/Users/chencgbv/Downloads/ALL_STUDENT_2016_JS.csv',
                               '/Users/chencgbv/Downloads/Suzhou_driver_1992.csv',
                               '/Users/chencgbv/Downloads/xiix_njutcm_urp.txt',
                               '/Users/chencgbv/Documents/njutcm_eol.csv',
                               '/Users/chencgbv/Documents/扬大XJ_XJB-2015-3-18.txt',
                               '/Users/chencgbv/Documents/南中医学生个人基本.csv'
                              ], selectors ):
        with open( datafile ) as alls:
            #content_list = alls.read().split('\n')
            #for x in content_list:
            #    if keyword in x.decode('utf8'):
            #       print x
            xs = filter( lambda _: True if keyword in _ else False, alls.read().decode('utf8').split('\n') )
            resultInfo += xs
    return resultInfo
'''
