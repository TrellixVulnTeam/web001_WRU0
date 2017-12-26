from django.shortcuts import render
from django.http import HttpResponse
from .models import PrivilegesInfo,LoginLog,UserInfo
import time
import traceback
# Create your views here.
def index(request):
    Localtime = time.localtime()
    Y = time.strftime("%Y", Localtime)
    M = time.strftime("%m", Localtime)
    D = time.strftime("%d", Localtime)
    H = time.strftime("%H:%M:%S", Localtime)
    Date = u"%s年%s月%s日 %s " %(Y,M,D,H)
    return render(request,'index.html',{'Date':Date})
def login(request):
    return render(request,'login.html')
#创建权限类型表
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
#创建用户
def createuser(request):
    user01 = {
    'GroupID':PrivilegesInfo.objects.get(GroupID=1),
    'LoginId':'admin',
    'Pwd':'admin',
    'Name':'alan',
    'Sex':'M',
    'Mail':'370220760@qq.com',
    'Phone':18079902120,
    'Address':'水贝万山',
    }
    user02 = {
    'GroupID':PrivilegesInfo.objects.get(GroupID=2),
    'LoginId':'aa',
    'Pwd':'123',
    }
    user03 = {
    'GroupID':PrivilegesInfo.objects.get(GroupID=3),
    'LoginId':'bb',
    'Pwd':'123',
    'Name': 'bb',
    }
    user04 = {
    'GroupID':PrivilegesInfo.objects.get(GroupID=6),
    'LoginId':'cc',
    'Pwd':'123',
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
def info(request):
    groupinfo = PrivilegesInfo.objects.all()
    userinfo = UserInfo.objects.all()
    return  HttpResponse('%s,%s'%(groupinfo,userinfo))