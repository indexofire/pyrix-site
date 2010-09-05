# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext as _
from django.forms.widgets import Media
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_slidershow.models import SliderPicture, SliderShow
from cmsplugin_slidershow.settings import *


class SliderShowPlugin(CMSPluginBase):
    """
    SliderShow Plugin Class.
    """
    model = SliderShow
    name = _('SliderShow')
    render_template = "cmsplugin_slidershow/slidershow.html"
    inlines = (SliderPictureAdmin, )

    '''
    class Media:
        """
        For a better user experience, we use a lightbox to edit inlines,
        hence the jquery-ui media inclusion.
        """
        css = {'all': ('%scss/jquery/cupertino/jquery-ui.css' % \
               settings.CMS_MEDIA_URL,)}
        js = ('%sjs/lib/ui.core.js' % settings.CMS_MEDIA_URL, 
              '%sjs/lib/ui.dialog.js' % settings.CMS_MEDIA_URL,)
    '''


    def render(self, context, instance, placeholder):
        """
        We provide 3 context variables for the rendering engines templates:
        * placeholder: the placeholder instance,
        * gallery: the gallery instance, 
        * settings: a dictionary of cmsplugin-gallery related settings.
        """
        context.update({
            'placeholder': placeholder,
            'cmsplugin_gallery_media_url': \
                CMSPLUGIN_GALLERY_MEDIA_URL,
            'slidershow': instance,
            'settings': {
                'thumbnail_size': (
                    CMSPLUGIN_GALLERY_THUMBNAIL_WIDTH,
                    CMSPLUGIN_GALLERY_THUMBNAIL_HEIGHT,
                ),
                'thumbnail_options': \
                    CMSPLUGIN_GALLERY_THUMBNAIL_OPTIONS,
                'show_gallery_title': \
                    CMSPLUGIN_GALLERY_SHOW_GALLERY_TITLE,
                'show_gallery_description': \
                    CMSPLUGIN_GALLERY_SHOW_GALLERY_DESCRIPTION,
            },
        })
        return context
    
    def get_plugin_media(self, request, context, plugin):
        return Media(
            css = {'all': ('cmsplugin_slidershow/css/slidershow.css',),},
            js = 
        )

plugin_pool.register_plugin(SliderShowPlugin)
