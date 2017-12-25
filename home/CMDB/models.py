from django.db import models

# Create your models here.
class PrivilegesInfo(models.Model):
    GroupID = models.CharField(max_length=20)
    Group = models.CharField(max_length=20)
class UserInfo(models.Model):
    UserID = models.AutoField(primary_key=True)
    GroupID = models.ForeignKey('PrivilegesInfo')
    LoginId = models.CharField(max_length=30)
    Pwd = models.CharField(max_length=30)
    Name = models.CharField(max_length=20)
    Sex = models.BooleanField(default=True)
    Phone = models.IntegerField()
    Address =models.CharField(max_length=100)
    CreateDate = models.DateTimeField(auto_now_add=True)
    LastLogin = models.DateTimeField(auto_now=True)
class LoginLog(models.Model):
    Id = models.AutoField(primary_key=True)
    UserID = models.ForeignKey('UserInfo')
    LoginIP = models.CharField(max_length=30)
    LoginStatus = models.BooleanField()
    LoginFail = models.IntegerField()
    LoginTime = models.DateTimeField(auto_now_add=True)