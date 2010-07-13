# -*- coding: utf-8 -*-
from django.conf import settings

# Wiki Index Name
DEFAULT_INDEX = getattr(settings, 'WIKI_DEFAULT_INDEX', 'WikiIndex')

# Wiki slug's regex
SLUG_REGEX = r'((([A-Z]+[a-z]+){2,})(/([A-Z]+[a-z]+){2,})*)'
SLUG = getattr(settings, 'WIKI_SLUG_REGEX', SLUG_REGEX)
