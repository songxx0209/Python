#!/usr/bin/python
#-*-coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from firstblog.models import Character

def staff(request):
    print 'okok=', Character
    staff_list = Character.objects.all()
    print 'list=', staff_list
    staff_str = map(str,staff_list)
    print 'okok11=', staff_str
    return HttpResponse("<p>"+' '.join(staff_str)+"</p>")

# 简单的接口
def logins(request):
    return HttpResponse('<h1>hello, world!</h1>')


def temp(request):
    return render(request, 'index.html', { 'a': 23, 'b': 32 })
