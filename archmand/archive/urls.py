# -*- coding=UTF-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns('archive.views',
    url(r'^$', 'home'),
    url(r'^login/$', 'login'),
    url(r'^test/(?P<pid>\d+)/$', 'test'),
)
