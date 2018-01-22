from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import PrivilegesInfo, LoginLog, UserInfo
from django.views.decorators.csrf import csrf_protect
import time
import os
import sys
import traceback
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from cmdb import elk
#获取当前时间
def DATE():
    Localtime = time.localtime()
    Y = time.strftime("%Y", Localtime)
    M = time.strftime("%m", Localtime)
    D = time.strftime("%d", Localtime)
    H = time.strftime("%H:%M:%S", Localtime)
    Now_Date = u"%s年%s月%s日 %s " % (Y, M, D, H)
    return Now_Date
# Create your views here.
# 创建用户组
def creategroup(reuqest):
    try:
        PrivilegesInfo.objects.create(Group='admin')
        PrivilegesInfo.objects.create(Group='sysadmin')
        PrivilegesInfo.objects.create(Group='dbadmin')
        PrivilegesInfo.objects.create(Group='netadmin')
        PrivilegesInfo.objects.create(Group='secadmin')
        PrivilegesInfo.objects.create(Group='user')
        print('OK')
        return HttpResponse('创建用户组成功')
    except:
        return HttpResponse('创建用户组出错')
        traceback.print_exc()
# 创建用户
def createuser(request):
    user01 = {
        'GroupID': PrivilegesInfo.objects.get(GroupID=1),
        'LoginId': 'admin',
        'Pwd': 'admin',
        'Name': 'alan',
        'Sex': 'M',
        'Mail': '370220760@qq.com',
        'Phone': 18079902120,
        'Address': '水贝万山',
    }
    user02 = {
        'GroupID': PrivilegesInfo.objects.get(GroupID=2),
        'LoginId': 'aa',
        'Pwd': '123',
    }
    user03 = {
        'GroupID': PrivilegesInfo.objects.get(GroupID=3),
        'LoginId': 'bb',
        'Pwd': '123',
        'Name': 'bb',
    }
    user04 = {
        'GroupID': PrivilegesInfo.objects.get(GroupID=6),
        'LoginId': 'cc',
        'Pwd': '123',
        'Name': 'cc',
    }
    try:
        UserInfo.objects.create(**user01)
        UserInfo.objects.create(**user02)
        UserInfo.objects.create(**user03)
        UserInfo.objects.create(**user04)
        return HttpResponse('创建用户成功')
        print('OK')
    except:
        return HttpResponse('创建用户出错,%s' % traceback.print_exc())
        traceback.print_exc()
# 用户登录
@csrf_protect
def login(request):
    if request.method == 'POST':
        LoginId = request.POST.get('username', None)
        Pwd = request.POST.get('pwd', None)
        if all([LoginId, Pwd]):
            Login = UserInfo.objects.filter(LoginId=LoginId, Pwd=Pwd).count()
            if Login == 1:
                login_info = {
                    'UserID': UserInfo.objects.get(LoginId=LoginId),
                    'LoginStatus': 'T'
                }
                try:
                    LoginLog.objects.create(**login_info)
                except:
                    traceback.print_exc()
                Localtime = time.localtime()
                Y = time.strftime("%Y", Localtime)
                M = time.strftime("%m", Localtime)
                D = time.strftime("%d", Localtime)
                H = time.strftime("%H:%M:%S", Localtime)
                Date = u"%s年%s月%s日 %s " % (Y, M, D, H)
                request.session['LoginId'] = LoginId
                #return render(request, 'index.html', {'Date': Date, 'username': LoginId})
                return redirect("/Dashboard/")
                #return HttpResponseRedirect("/Dashboard/")
            else:
                Login = UserInfo.objects.filter(LoginId=LoginId).count()
                if Login == 1:
                    login_info = {
                        'UserID': UserInfo.objects.get(LoginId=LoginId),
                        'LoginStatus': 'F'
                    }
                    try:
                        LoginLog.objects.create(**login_info)
                        return render(request, 'login.html', {'hint': "账号或密码错误请重新输入"})
                    except:
                        traceback.print_exc()
                        return render(request, 'login.html', {'hint': "账号或密码错误请重新输入"})

                else:
                    return render(request, 'login.html', {'hint': "账号不存在"})
        else:
            return render(request, 'login.html', {'hint': "账号或密码不允许为空"})
    else:
        return render(request, 'login.html')
#CMDB页面
# data_list = []
# city = '长沙'
# num = 90
# data_format = [{'name':'上海'},{'name':'%s' % city,'value':num}]
# data_list.append(data_format)

def dashboard(request, Html='index'):
    URL = Html
    Date = DATE()
    data_list = []
    data_info = elk.run(Date_limt=30,size=20)
    username = request.session.get('LoginId')
    if username:
        if Html == 'index':
            for k, v in data_info.items():
                data_format = [{'name': '上海'}, {'name': '%s' % k, 'value': v}]
                data_list.append(data_format)
            print(data_list)
            data = json.dumps(data_list, ensure_ascii=False)
            return render(request, "%s.html" % URL, {'Date': Date, 'username': username ,'data':data})
        else:
            return render(request, "%s.html" % URL, {'Date': Date, 'username': username})
    else:
        return redirect("/login/")
# 获取用户与用户组
def info(request):
    groupinfo = PrivilegesInfo.objects.all()
    userinfo = UserInfo.objects.all()
    return HttpResponse('%s,%s' % (groupinfo, userinfo))
#获取用户信息
def Data(request):
    User = UserInfo.objects.all()
    return render(request, 'list.html', {'data': User})
