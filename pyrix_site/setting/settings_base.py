# -*- coding: utf-8 -*-
# Django settings for pyrix project.
import os
from settings import PROJECT_PATH


ADMINS = (
    ('WebMaster', 'webmaster@localhost.com'),
)

#CACHE_BACKEND = 'locmem://127.0.0.1:11211/'

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '87=llta=149jepze@g#fa^m#hzu^mv%@8+%fd5p)*1$(*tvbh6'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    #'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
    'onlineuser.middleware.OnlineUserMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'cms_content.middleware.FrontEndPublishMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'cms.context_processors.media',
    'forum.context_processors.page_size',
    #'cms_content.context_processors.content_page',
)

ROOT_URLCONF = 'pyrix.urls'
INTERNAL_IPS = ('127.0.0.1',)

THEME_PATH = 'themes/planet/templates/'
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates/%s' % THEME_PATH),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.comments',
    'django.contrib.sitemaps',
    'cms',
    'mptt',
    'publisher',
    'menus',
    'cms.plugins.text',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cmsplugin_rst',
    'cmsplugin_gallery',
    'cms_content.plugins',
    #'south',
    'reversion',
    'dbgettext',
    'cms_content',
    'debug_toolbar',
    'registration',
    'pagination',
    #'user_profile',
    'userprofile',
    'wiki',
    'forum',
    'attachments',
    #'onlineuser',
    'simpleavatar',
    'account',
    #'djangohelper',
    'haystack',
    'taggit',
    'easy_thumbnails',
    'templatetag_sugar',
)
