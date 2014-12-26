# -*- coding=UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect

from archive.models import Archive
from userman.models import User


def home(request):
    if request.method == 'POST':
        _id = request.POST['identity']
        try:
            _archive = Archive.objects.get(archive=_id)
        except:
            pass
        else:
            print(_archive.archive, _archive.identity)
            return redirect('/archive/%s' % _archive.archive)
        try:
            _archive = Archive.objects.get(identity=_id)
        except:
            pass
        else:
            print(_archive.archive, _archive.identity)
            return redirect('/archive/%s' % _archive.archive)
    if not request.session.get('user'):
        return redirect('/login')
    context = {'user': request.session.get('user')}
    return render(request, 'userman/home.html', context)


def login(request):
    if request.method == 'POST':
        _acc = request.POST['account']
        _pass = request.POST['password']
        try:
            u = User.objects.get(account=_acc, password=_pass)
        except:
            return redirect('/login')
        u = {'id': u.id,
            'name': u.name}
        request.session['user'] = u
        return redirect('/')
    return render(request, 'userman/login.html')


def logout(request):
    try:
        del request.session['user']
    except:
        pass
    return redirect('/login')
