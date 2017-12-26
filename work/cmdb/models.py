from django.db import models

#python manage.py makemigrations 检查变更
#python manage.py migrate        创建数据库表
# Create your models here.
class PrivilegesInfo(models.Model):
    GroupID = models.AutoField(primary_key=True)
    Group = models.CharField(max_length=20)
class UserInfo(models.Model):
    UserID = models.AutoField(primary_key=True)
    GroupID = models.ForeignKey('PrivilegesInfo')
    LoginId = models.CharField(max_length=30,unique=True)
    Pwd = models.CharField(max_length=30)
    Name = models.CharField(max_length=20)
    Sex_Choice = (
        (u'M',u'男'),
        (u'F',u'女'),
    )
    Sex = models.CharField(max_length=4,choices=Sex_Choice,null=True)
    Mail = models.EmailField(null=True)
    Phone = models.IntegerField(null=True)
    Address =models.CharField(max_length=100,null=True)
    CreateDate = models.DateTimeField(auto_now_add=True)
    LastLogin = models.DateTimeField(auto_now=True)
class LoginLog(models.Model):
    Id = models.AutoField(primary_key=True)
    UserID = models.ForeignKey('UserInfo')
    LoginIP = models.GenericIPAddressField(null=True)
    Status = (
        (u'T',u'Success'),
        (u'F',u'Fail'),
    )
    LoginStatus = models.CharField(max_length=10,choices=Status,null=True)
    LoginFail = models.IntegerField(null=True)
    LoginTime = models.DateTimeField(auto_now_add=True)