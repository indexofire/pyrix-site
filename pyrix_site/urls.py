# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps import Sitemap 
from cms_content.models import CMSArticle
from cms_content.settings import ROOT_URL


admin.autodiscover()

class ArticleSiteMap(Sitemap):  
    changefreq = 'daily' 

    def items(self): 
        return CMSArticle.objects.filter(pub_status='pub')

    def lastmod(self, obj): 
        return obj.created_date

    def location(self, obj):
        return ROOT_URL + 'article/' + "%s/%s/%s/%s/" % (
            obj.created_date.strftime('%Y'),
            obj.created_date.strftime('%m'),
            obj.created_date.strftime('%d'),
            obj.slug,
            )


sitemaps = {
    'article': ArticleSiteMap,
}


urlpatterns = patterns('',
    (r'^favicon\.ico$', redirect_to, {'url': '/media/favicon.ico'}),
    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    (r'^comment/', include('django.contrib.comments.urls')),
    #(r'^wiki/', include('wiki.urls')),
    (r'^member/', include('userprofile.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^attachments/', include('attachments.urls')),
    url(r'^avatar/', include('simpleavatar.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^help/$', direct_to_template, {'template': 'help.html', 'mimetype': 'text/html'}, name='help_page'),
    url(r'^about/$', direct_to_template, {'template': 'about.html', 'mimetype': 'text/html'}, name='about_page'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
	    url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,},
        ),
    )

urlpatterns += patterns('',
    (r'^', include('cms.urls')),
)
