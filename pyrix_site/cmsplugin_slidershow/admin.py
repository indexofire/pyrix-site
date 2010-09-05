# -*- coding: utf-8 -*-
from django.contrib import admin
from cmsplugin_slidershow.models import SliderPicture

class SliderPictureAdmin(admin.StackedInline):
    """
    Photo admin class that will be displayed as inline in the gallery admin.
    """
    model = SliderPicture

    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        Method to tweak the widgets attributes.
        """
        field = super(SliderPictureAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'description':
            field.widget.attrs['rows'] = 2
        return field
