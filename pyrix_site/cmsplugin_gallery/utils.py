"""
cmsplugin_gallery utils.
"""

from cmsplugin_gallery import settings


def get_rendering_engine_choices():
    """
    Return the list of rendering engines in a tuple compatible with django 
    charfield choices.
    """
    return settings.CMSPLUGIN_GALLERY_RENDERING_ENGINES
