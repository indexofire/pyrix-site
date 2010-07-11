# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from cms_content.menu import CMSSectionMenu


class Wiki(CMSApp):
    name = _(u"Wiki Page")
    urls = ["wiki.urls"]
    #menus = [WikiMenu]

apphook_pool.register(Wiki)
