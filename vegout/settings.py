# -*- coding: utf-8 -*-
"""
Django settings for vegout project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3l8-hcq4$+itfs@6s0oj*u%1aa0w(b%i2br9v2rgi$k-lt-*u&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_pdb',
    'restaurant',
    'bootstrap3',
    'leaflet',
    'taggit',
    'jstemplate',
    'analytical',
)

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (50.6407351, 4.66696),
    'DEFAULT_ZOOM': 8,
    'MIN_ZOOM': 8,
    'MAX_ZOOM': 19,
    'RESET_VIEW': False,

    # https://www.mapbox.com/mapbox.js/example/v1.0.0/plain-leaflet/
    'TILES': "https://api.mapbox.com/v4/mapbox.streets/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiZHJ6cmFmIiwiYSI6ImNpaDUwdnl2cTB6b2N2a201aWFidmlnYzIifQ.QA_mphcWhdwAh6sgdAzdcg",
    # https://www.mapbox.com/help/attribution/
    'ATTRIBUTION_PREFIX': "© <a href='https://www.mapbox.com/map-feedback/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap contributors</a>",

    'PLUGINS': {
        'locate': {
            'css': ['css/L.Control.Locate.css'],
            'js': 'js/L.Control.Locate.js',
            'auto-include': True,
        },
        'awesome_markers': {
            'css': ['css/leaflet.awesome-markers.css'],
            'js': 'js/leaflet.awesome-markers.min.js',
            'auto-include': True,
        },
        'makercluster': {
            'css': ['css/MarkerCluster.Default.css', 'css/MarkerCluster.css'],
            'js': 'js/leaflet.markercluster.js',
            'auto-include': True,
        },
    },
}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'vegout.context_processors.flavour',
            ],
            'loaders': [
                'hamlpy.template.loaders.HamlPyFilesystemLoader',
                'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

ROOT_URLCONF = 'vegout.urls'

WSGI_APPLICATION = 'vegout.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

JSTEMPLATE_DIRS = [ os.path.join(BASE_DIR, 'restaurant', 'templates') ]

VEGO_RESTO = False
APP_NAME = "Manger Veggie"
ANDROID_APP_URL = "https://play.google.com/store/apps/details?id=be.desmottes.mangerveggie"

PIWIK_SITE_ID = 0
PIWIK_DOMAIN_PATH = "example.com"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

try:
    from settings_local import *
except ImportError:
    pass

if DEBUG == False:
    TEMPLATES[0]["OPTIONS"]["loaders"] = [
        ('django.template.loaders.cached.Loader', (
            'hamlpy.template.loaders.HamlPyFilesystemLoader',
            'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
        )),
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]
