from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
# Create your views here.
def index(request):
    return HttpResponse("Hello,World")
def hello(request):
    return render(request,"R.html")
def hi(request):
    return render(request,'index.html')
def register(request):
    name = request.POST['username']
    pwd = request.POST['pwd']
    phone = request.POST['phone']
    print(name,pwd,phone)
    return render(request,"register.html")
