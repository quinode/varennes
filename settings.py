# -*- coding:utf-8 -*-

import os
DIRNAME = os.path.dirname(__file__)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dominique Guardiola', 'web@quinode.fr'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'varennes',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

import locale
locale.setlocale(locale.LC_ALL,'')
import django.conf.global_settings as DEFAULT_SETTINGS

DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CHARSET='utf-8'

AUTH_PROFILE_MODULE = 'fcpe.adherent'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'


MEDIA_ROOT = os.path.join(DIRNAME,'static/uploads/')
MEDIA_URL = '/static/uploads/'

STATIC_ROOT = os.path.join(DIRNAME,'static_collected/')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

import admin_tools
ADMIN_TOOLS_PATH = os.path.dirname(os.path.abspath(admin_tools.__file__))


IMAGE_FOLDER = 'image'
DOCUMENT_FOLDER = 'document'

STATICFILES_DIRS = (
    os.path.join(DIRNAME,'static/'),
    os.path.join(ADMIN_TOOLS_PATH,'media/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(sb++sngrtpoj1^jr&u1kxh$c2vl58+mirk7i4@7o+ad4%=l9='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'varennes.urls'



TEMPLATE_DIRS = (
    os.path.join(DIRNAME+'/templates/'),    
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    'django.core.context_processors.request',
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)

INSTALLED_APPS = (

    # Admin tools
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Coop CMS
    'livesettings',
    'sorl.thumbnail',
    'floppyforms',
    'html_field',
    'djaloha',
    'coop_cms',

)


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

 
CACHE_MIDDLEWARE_KEY_PREFIX = DIRNAME
CACHES = {
     'default': {
         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
     }
 }


LIVESETTINGS_OPTIONS = \
 {
     1: {
     'DB': True,
        'SETTINGS': {
             u'coop_cms': {u'CONTENT_APPS': u'["coop_cms"]'}
         }
     }
 }


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError, exp:
    pass

