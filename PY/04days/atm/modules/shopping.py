#!/usr/bin/env python
#-*- coding:utf-8 -*-
#__author__ = "Alan"
import  json
import os
import sys
import getpass
#'获取目录'
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if sys.platform == 'linux':
    user_db = base_dir + r'/db/users_info'
    creditcard_db = base_dir + r'/db/creditcard_info'
else:
    user_db = base_dir + r'\db\users_info'
    creditcard_db = base_dir + r'\db\creditcard_info'
def count(Count,Error):
    if Count == 3:
        print('输入错误超过3次，退出程序')
    else:
        print('%s' % Error)
