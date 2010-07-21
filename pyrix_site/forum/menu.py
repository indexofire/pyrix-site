# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

#from forum.settings import ROOT_URL
from forum.models import *


class ForumMenu(CMSAttachMenu):
    name = _(u"Discussion Board Menu")
    
    def get_nodes(self, request):
        nodes = []
        forums = Forum.objects.all().select_related()
        count = forums.count()+1
        for forum in forums:
            url = '/forum/forum/' + forum.slug
            nodes.append(NavigationNode(forum.name, url, forum.pk))
            topics = Topic.objects.select_related('forum').filter(forum__pk=forum.pk)
            for topic in topics:
                url = '/forum/topic/' + str(topic.pk) + '/'
                nodes.append(NavigationNode(topic.subject, url, count, topic.forum_id))
                count += 1
        return nodes

menu_pool.register_menu(ForumMenu)
