# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from wiki.menu import WikiPageMenu


class WikiApp(CMSApp):
    name = _(u"Wiki Page App")
    urls = ["wiki.urls"]
    menus = [WikiPageMenu]

apphook_pool.register(WikiApp)
