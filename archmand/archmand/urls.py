# -*- coding=UTF-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'archmand.views.home', name='home'),
    # url(r'^archmand/', include('archmand.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url('', include('archive.urls')),
    url('', include('userman.urls')),
    # url(r'^test/(?P<pid>\d+)/$', 'archive.views.test')
)
