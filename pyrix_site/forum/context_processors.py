# -*- coding: utf-8 -*-
from django.conf import settings

from forum.settings import CTX_CONFIG

def page_size(request):
    context = {}
    if hasattr(settings, 'FORUM_CTX_CONFIG'):
        context['FORUM_PAGE_SIZE'] = settings.FORUM_CTX_CONFIG['FORUM_PAGE_SIZE']
        context['TOPIC_PAGE_SIZE'] = settings.FORUM_CTX_CONFIG['TOPIC_PAGE_SIZE']
    return context

