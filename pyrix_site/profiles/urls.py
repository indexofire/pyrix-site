# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from profiles.views import *

urlpatterns = patterns('',
    url(r'^$', profile_list, name='profile_list'),
    url(r'^edit/$', profile_edit, name='profile_edit'),
    url(r'^(?P<username>[-\w]+)/$', profile_detail, name='profile_detail'),
)
