# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^favicon.ico/$', redirect_to, {'url': '/media/favicon.ico'}),
    #(r'^robots.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    (r'^accounts/', include('registration.backends.default.urls')),
    #(r'^blog/', include('zinnia.urls')),
    (r'^comment/', include('django.contrib.comments.urls')),
    (r'^wiki/', include('wiki.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('',
	    url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,},
        ),
    )

urlpatterns += patterns('',
    (r'^', include('cms.urls')),
)
