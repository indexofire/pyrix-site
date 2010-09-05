# -*- coding: utf-8 -*-
import os
from django.db import models
from django.utils.translation import ugettext as _
from cms.models import CMSPlugin
from cmsplugin_slidershow import settings, utils


class SliderShow(CMSPlugin):
    """
    Class that represents a SliderShow.

    Property:
    ``title``
        The gallery title, if given it will be displayed in the gallery 
        header (optional).

    ``render_template``
        The rendering engine to use for the gallery, this is a template path.

    You can retrieve the list of active photos with the ``active_photos`` 
    convenience method.
    """

    title = models.CharField(
        _(u'title'),
        max_length=50,
        blank=True,
        help_text=_("The slidershow's title, if given it will be displayed in the gallery header (optional)")
    )
    render_template = models.CharField(
        _(u'rendering engine'),
        max_length=255,
        choices=utils.get_rendering_engine_choices(),
        help_text=_("The rendering engine to use for the slidershow")
    )

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')

    def __unicode__(self):
        if self.title:
            return self.title
        return u'%s #%s' % (_('gallery'), self.id)

    def active_photos(self):
        """
        Return the active photos queryset.
        """
        return self.photo_set.filter(active=True)


class SliderPicture(models.Model):
    """
    Class that represent a photo of the gallery, photos have the following
    properties:

    ``title``
        The photo title (required).

    ``description``
        A description for the photo (optional).

    ``image``
        The image, thumbnail will be generated with this image (required).

    ``link``
        A link to add to the image (optional).

    ``active``
        A boolean that allows to deactivate an image without removing it 
        completely, if set to ``False``, the photo will not appear in the
        gallery (default: True).

    ``order``
        An integer representing the order (position) of the photo in the
        gallery (default: 0).
    """

    slidershow = models.ForeignKey(SliderShow)

    title = models.CharField(
        _(u'title'),
        max_length=250,
        help_text=_('A descriptive title for your photo')
    )
    description = models.TextField(
        _(u'description'), 
        blank=True, 
        help_text=_('An optional description for your photo')
    )
    image = models.ImageField(
        _('image'),
        upload_to=settings.CMSPLUGIN_GALLERY_UPLOAD_DIR,
        help_text=_('Please upload a jpeg or png image')
    )
    link = models.CharField(
        _('Link'),
        blank=True,
        max_length=250,
        help_text="A link to add to your photo"
    )
    active = models.BooleanField(
        _('Active'), 
        default=True,
        help_text=_('Uncheck this to deactivate the photo in the gallery '\
                    'without removing it'))
    order = models.IntegerField(_('Order'), blank = True, null = True)

    class Meta:
        verbose_name = _('photo')
        verbose_name_plural = _('photos')
        ordering = ('order',)

    def __unicode__(self):
        return self.title
