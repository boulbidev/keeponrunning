########################################################################################################################
# keeponrunning/config/settings/settings.py
########################################################################################################################
import os
import environ
from adminutils.utils import str_to_boolean

########################################################################################################################
# Les objets répertoire (du module django-environ, pas de Python)
# root_dir représente l'objet source du projet
# apps_dir représente l'objet source de l'app
root_dir = environ.Path(__file__) - 3
apps_dir = root_dir.path(os.environ['PROJECT_NAME'])
########################################################################################################################

########################################################################################################################
# Les basiques
# SECRET CONFIGURATION
SECRET_KEY = os.environ['SECRET_KEY']

# DEBUG
DEBUG = str_to_boolean(os.environ['DEBUG'])

if os.environ['ENV_UTILISE'] == 'PROD':
    ALLOWED_HOSTS = [os.environ['ALLOWED_HOSTS']]
else:
    ALLOWED_HOSTS = []
########################################################################################################################

########################################################################################################################
# Applications et middleware
INSTALLED_APPS = [
    'home',
    'search',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]
########################################################################################################################

########################################################################################################################
# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [apps_dir('templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
########################################################################################################################

########################################################################################################################
# URL Configuration
ROOT_URLCONF = 'config.urls'
########################################################################################################################

########################################################################################################################
# WSGI
WSGI_APPLICATION = 'config.wsgi.application'
########################################################################################################################


########################################################################################################################
# Database
if os.environ['ENV_UTILISE'] == 'PROD':
    DATABASES = {"default": {"ENGINE": "django.db.backends.postgresql_psycopg2", }}
else:
    DATABASES = {
        'default': {
            'ENGINE': os.environ['DATABASE_ENGINE'],
            'NAME': os.environ['DATABASE_NAME'],
            'ADMIN': os.environ['DATABASE_ADMIN'],
            'PASSWORD': os.environ['DATABASE_PASSWORD'],
            'HOST': os.environ['DATABASE_HOST'],
            'PORT': os.environ['DATABASE_PORT'],
        }
    }
########################################################################################################################

########################################################################################################################
# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
########################################################################################################################

########################################################################################################################
# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True
########################################################################################################################


########################################################################################################################
# STATIC FILE  AND MEDIA FILES CONFIGURATION
# STATIC_ROOT est le répertoire utilisé pour regrouper les fichiers static avec la commande collectstatic
# Idem pour MEDIA_ROOT
STATICFILES_LOCATION = 'static'
STATIC_ROOT = root_dir(STATICFILES_LOCATION)
MEDIAFILES_LOCATION = 'media'
MEDIA_ROOT = apps_dir(MEDIAFILES_LOCATION)

# STATICFILES_DIRS est la liste des différents répertoires contenant des fichiers statiques
STATICFILES_DIRS = [
    apps_dir(STATICFILES_LOCATION),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
########################################################################################################################

########################################################################################################################
# Wagtail settings
WAGTAIL_SITE_NAME = "keeponrunning"
########################################################################################################################

########################################################################################################################
# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://keeponrunning.com'
########################################################################################################################

