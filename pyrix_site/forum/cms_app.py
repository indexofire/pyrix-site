# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
#from forum.menu import ForumMenu


class ForumApp(CMSApp):
    name = _(u"Disscusion Board")
    urls = ["forum.urls"]
    #menus = [ForumMenu]
    
apphook_pool.register(ForumApp)
