from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^user',views.createuser),
    url(r'^group',views.creategroup),
    url(r'^info',views.info),
]