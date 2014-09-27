# -*- coding=UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    if not request.session.get('user'):
        return redirect('/login')
    user = {'name': 1123}
    context = {'user': user}
    return render(request, 'archive/home.html', context)


def login(request):
    if request.method == 'POST':
        pass

    return render(request, 'archive/login.html')


def test(request, pid):
    return HttpResponse("You're looking at the results of test %s." % pid)
