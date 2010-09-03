"""
cmsplugin_gallery plugin admin.
"""

from django.contrib import admin
from django.utils.translation import ugettext as _
from django.forms.widgets import Media
from django.conf import settings
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_gallery.models import Gallery, Photo
from cmsplugin_gallery import settings as plugin_settings


class PhotoAdmin(admin.StackedInline):
    """
    Photo admin class that will be displayed as inline in the gallery admin.
    """
    model = Photo

    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        Method to tweak the widgets attributes.
        """
        field = super(PhotoAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            field.widget.attrs['rows'] = 2
        return field


class GalleryPlugin(CMSPluginBase):
    """
    Gallery admin class.
    """
    model = Gallery
    name = _('Gallery')
    inlines = (PhotoAdmin, )

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
                plugin_settings.CMSPLUGIN_GALLERY_MEDIA_URL,
            'gallery': instance,
            'settings': {
                'thumbnail_size': (
                    plugin_settings.CMSPLUGIN_GALLERY_THUMBNAIL_WIDTH,
                    plugin_settings.CMSPLUGIN_GALLERY_THUMBNAIL_HEIGHT,
                ),
                'thumbnail_options': \
                    plugin_settings.CMSPLUGIN_GALLERY_THUMBNAIL_OPTIONS,
                'show_gallery_title': \
                    plugin_settings.CMSPLUGIN_GALLERY_SHOW_GALLERY_TITLE,
                'show_gallery_description': \
                    plugin_settings.CMSPLUGIN_GALLERY_SHOW_GALLERY_DESCRIPTION,
            },
        })
        return context


# register the plugin with the django-cms plugin framework
plugin_pool.register_plugin(GalleryPlugin)
