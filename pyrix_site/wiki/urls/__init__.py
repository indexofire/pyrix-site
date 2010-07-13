# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from wiki.views import *
from wiki.settings import SLUG


urlpatterns = patterns('',
    # Wiki Index
    url(r'^$', index, name='wiki_index'),

    # Revision and Page list
    url(r'^history/$', revision_list, name='wiki_revision_list'),
    url(r'^index/$', page_list, name='wiki_page_list'),

    # Revision list for page
    url(r'^(?P<slug>%s)/history/$' % SLUG, 
        revisions, name='wiki_revision_list'),

    # Changes between two revisions, revision id's come from GET
    url(r'^(?P<slug>%s)/changes/$' % SLUG, changes, name='wiki_changes'),

    # Edit Form
    url(r'^(?P<slug>%s)/edit/(?P<rev_id>\d+)/$' % SLUG,
        login_required(edit), name='wiki_edit'),
    url(r'^(?P<slug>%s)/edit/$' % SLUG, login_required(edit), name='wiki_edit'),

    # Page
    url(r'^(?P<slug>%s)/rev(?P<rev_id>\d+)/$' % SLUG, page, name='wiki_page'),
    url(r'^(?P<slug>%s)/$' % SLUG, page, name='wiki_page'),
)
