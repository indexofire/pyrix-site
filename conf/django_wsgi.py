#!/usr/bin/env python
import os, sys
import django.core.handlers.wsgi
sys.path.append('/home/mark/www/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
