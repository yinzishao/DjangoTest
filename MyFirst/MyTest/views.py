#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
 
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def home(request):
    string = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request,'home.html',{'string':string})

def index(reuqest):
    return render(reuqest, 'index.html')


def columns(request):
    return render(request, 'blog/index.html')