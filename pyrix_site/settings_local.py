# -*- coding: utf-8 -*-

gettext = lambda s: s

# django-cms-2.0 Settings:
APPEND_SLASH = True
CMS_SOFTROOT = True
CMS_MODERATOR = False
CMS_PERMISSION = True
CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_FLAT_URLS = False
CMS_MENU_TITLE_OVERWRITE = True
CMS_HIDE_UNTRANSLATED = False
CMS_URL_OVERWRITE = True
LANGUAGES = (
    ('en', gettext('English')),
    ('zh-cn', gettext("Chinese")),
)
CMS_TEMPLATES = (
    ('base.html', gettext('default')),
    ('col_two.html', gettext('two columns')),
    ('col_three.html', gettext('three columns')),
    ('nav_playground.html', gettext('navigation examples')),
)
CMS_PLACEHOLDER_CONF = {
    'col_sidebar': {
        'plugins': (
            'TextPlugin',
            'LinkPlugin',
            'LatestArticlePlugin',
        ),
        'name': gettext("sidebar column"),
    },
    'col_left': {
        'plugins': (
            'TextPlugin',
            'GoogleMapPlugin',
            'ReSTPlugin',
            'PicturePlugin',
            'LinkPlugin',
        ),
        'name': gettext("left column"),
    },
    'col_right': {
        'plugins': (
            'LinkPlugin',
            'PicturePlugin',
            'TextPlugin',
            'GoogleMapPlugin',
            'ReSTPlugin', 
        ),
        'name': gettext("right column"),
    },
}

# south
SOUTH_TESTS_MIGRATE = False

# cms_content
CMS_CONTENT_EDITOR = 'WYMEditor'
CMS_CONTENT_ROOT_URL = '/cms/'
CMS_CONTENT_CODE_HIGHLIGHT = True
CMS_CONTENT_CODE_HIGHLIGHT_CSS = 'code_highlight'
CMS_CONTENT_CODE_HIGHLIGHT_LINENOS = True

AKISMET_API_KEY = '773ea92115d8'

# django-registration
ACCOUNT_ACTIVATION_DAYS = 14

# user_profile
AUTH_PROFILE_MODULE = 'forum.ForumUserProfile'

# haystack
HAYSTACK_SITECONF = 'pyrix.search_site'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = 'search_index'

# reCapture
RECAPTCHA_PRIVATE_KEY = '6LfIO7wSAAAAAPPt4nVtrUIzFc49_FQoM1MT_i0r'

# forum
FORUM_CTX_CONFIG = {
    'FORUM_TITLE': 'HZCDCLabs Forum',
    'FORUM_SUB_TITLE': '',
    'FORUM_PAGE_SIZE': 50,
    'TOPIC_PAGE_SIZE': 20,
}
