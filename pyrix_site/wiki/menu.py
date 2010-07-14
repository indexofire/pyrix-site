# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

from cms.menu_bases import CMSAttachMenu

from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from wiki.models import WikiPage

class WikiPageMenu(CMSAttachMenu):
    """Wiki Page Menu
    
    Create a Wiki Page menu in breadcrumb.
    """
    name = _("Wiki Page Menu")

    def get_nodes(self, request):
        nodes=[]
        wikipages = WikiPage.objects.all()
        for wikipage in wikipages:
            nodes.append(NavigationNode(wikipage.slug, 
                wikipage.slug, 
                wikipage.pk))
        return nodes


menu_pool.register_menu(WikiPageMenu)

