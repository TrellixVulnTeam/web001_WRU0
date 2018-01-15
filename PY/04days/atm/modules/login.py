#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = "Alan"
import os,sys,json,getpass
#'获取用户数据'
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if sys.platform == 'linux':
    user_db = base_dir + r'/db/users_info'
    creditcard_db = base_dir + r'/db/creditcard_info'
else:
    user_db = base_dir + r'\db\users_info'
    creditcard_db = base_dir + r'\db\creditcard_info'
#'错误显示'
def count(Count,Error):
    if Count == 3:
        print('输入错误超过3次，退出程序')
    else:
        print('%s' % Error)
#'登录函数'
def login_auth(res,file=user_db,hint='账号',name='username',pwd='pwd'):
    Count = 0
    while Count < 3:
        username = input("请输入您的%s:" % hint)
        if len(username.strip()) > 0:
            with open(file, 'r+') as read_user_info:
                user_list = json.loads(read_user_info.read())
                if username in user_list:
                    if user_list.get(username).get('locked') == 0:
                        while Count < 3:
                            pwd = getpass.getpass("请输入您的密码:")
                            if pwd == user_list.get(username).get('password'):
                                print("验证成功，欢迎使用")
                                return res, username
                            else:
                                Count+=1
                                Error = "密码错误，请重新输入"
                                count(Count, Error)
                                if Count == 3:
                                    user_list.get(username)['locked'] = 1
                                    print("输入密码错误超过三次,%s已锁定，请联系管理员解锁" %hint)
                    else:
                        Count+=1
                        Error = "%s已锁定，请联系管理员解锁" % hint
                        count(Count, Error)
                        break
                else:
                    Count+=1
                    Error = "%s不存在，请重新输入" %hint
                    count(Count, Error)
            with open(file,'w') as writ_user_info:
                writ_user_info.write(json.dumps(user_list))
                writ_user_info.flush()
                writ_user_info.close()
        else:
            Count += 1
            Error = "%s不能为空" %hint
            count(Count,Error)
#'登录模块'
def login(auth_type):
    def wrapper(func):
        if auth_type == 'user':
            def auth_user():
                res = func()
                login_auth(res)
            return auth_user
        if auth_type == 'admin':
            def admin_auth():
                res = func()
                login_auth(res)
            return admin_auth
        if auth_type == 'creditcard':
            def creditcard_auth():
                res = func()
                login_auth(res,file=creditcard_db,name='creditcard',hint='信用卡')
            return creditcard_auth
        else:
            print("请先定义认证方式")
    return wrapper
#'用户登录验证'
@login(auth_type='user')
def user_login():
    print("用户登录认证")
    return True
#'后台管理用户登录验证'
@login(auth_type='admin')
def admin_login():
    print("后台管理中心登录认证")
    return True
#'信用卡登录验证'
@login(auth_type='creditcard')
def creditcard_login():
    print("信用卡认证")
    return True

