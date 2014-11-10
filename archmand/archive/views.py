# -*- coding=UTF-8 -*-

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from archive.models import Archive
from userman.models import User


def test(request, pid):
    u = User.objects.all()
    print(u[0].name)
    return HttpResponse("You're looking at the results of test %s." % pid)


def search_archive(request):
    _identity = request.POST['identity']
    try:
        archive = Archive.objects.get(
            Q(archive=_identity) | Q(identity=_identity))
    except:
        return redirect('/')
    print(archive.name)
    return redirect('/archive/%s' % archive.archive)
