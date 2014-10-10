# -*- coding=UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect

from userman.models import User

def test(request, pid):
    u = User.objects.all()
    print(u[0].name)
    return HttpResponse("You're looking at the results of test %s." % pid)
