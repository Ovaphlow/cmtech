# -*- coding=UTF-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns('userman.views',
    url(r'^$', 'home'),
    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),
)
