from django.contrib import admin
from .models import UserInfo,PrivilegesInfo,LoginLog
#python manage.py createsuperuser
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(PrivilegesInfo)
admin.site.register(LoginLog)