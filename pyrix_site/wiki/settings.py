# -*- coding: utf-8 -*-
from django.conf import settings


DEFAULT_INDEX = getattr(settings, 'WIKI_DEFAULT_INDEX', 'WikiIndex')
