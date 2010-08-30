# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from account.views import *


urlpatterns = patterns('',
    url(r'^$', login_required(views.profile), name='account_index'),
    url(r'^signature/$', signature, name='signature'),
    (r'^', include('registration.backends.default.urls')),
)
