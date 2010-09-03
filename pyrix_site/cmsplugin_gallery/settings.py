"""
cmsplugin-gallery settings.
You can override all these settings in your local settings.py file.
"""

from django.conf import settings

# dummy gettext for l10n in settings
gettext = lambda s: s

# Directory where to store cmsplugin_gallery images
CMSPLUGIN_GALLERY_MEDIA_URL = getattr(
    settings,
    'CMSPLUGIN_GALLERY_MEDIA_URL',
    '%s/%s' % (getattr(settings, 'STATIC_URL', settings.MEDIA_URL), 'cmsplugin_gallery')
)

# Directory where to store cmsplugin_gallery images
CMSPLUGIN_GALLERY_UPLOAD_DIR = getattr(
    settings,
    'CMSPLUGIN_GALLERY_UPLOAD_DIR',
    'uploads/cmsplugin_gallery'
)

# default width of the generated thumbnails
CMSPLUGIN_GALLERY_THUMBNAIL_WIDTH = getattr(
    settings,
    'CMSPLUGIN_GALLERY_THUMBNAIL_WIDTH',
    80
)

# default height of the generated thumbnails
CMSPLUGIN_GALLERY_THUMBNAIL_HEIGHT = getattr(
    settings,
    'CMSPLUGIN_GALLERY_THUMBNAIL_HEIGHT',
    80
)

# thumbnails options
CMSPLUGIN_GALLERY_THUMBNAIL_OPTIONS = ['sharpen', 'crop']

# whether to show the gallery title or not
CMSPLUGIN_GALLERY_SHOW_GALLERY_TITLE = getattr(
    settings,
    'CMSPLUGIN_GALLERY_SHOW_GALLERY_TITLE',
    True
)

# whether to show the gallery description or not
CMSPLUGIN_GALLERY_SHOW_GALLERY_DESCRIPTION = getattr(
    settings,
    'CMSPLUGIN_GALLERY_SHOW_GALLERY_DESCRIPTION',
    True
)

# list of rendering engines
CMSPLUGIN_GALLERY_RENDERING_ENGINES = getattr(
    settings,
    'CMSPLUGIN_GALLERY_RENDERING_ENGINES',
    [
        ('cmsplugin_gallery/none.html', gettext('None (html only)'),),
        ('cmsplugin_gallery/easyslider.html', gettext('Easy slider'),),
        ('cmsplugin_gallery/galleria.html', gettext('Galleria'),),
        ('cmsplugin_gallery/galleriffic.html', gettext('Galleriffic'),),
        ('cmsplugin_gallery/pickachoose.html', gettext('Pickachoose'),),
    ]
)
