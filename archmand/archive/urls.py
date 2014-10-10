# -*- coding=UTF-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns('archive.views',
    url(r'^test/(?P<pid>\d+)/$', 'test'),
)
