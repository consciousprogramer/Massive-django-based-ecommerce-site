"""
Django settings for ecom project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.contrib.messages import constants as messages


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_ECOM_SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get("DJANGO_ECOM_ENV") == "dev":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    '127.0.0.1',
]
# Application definition

INSTALLED_APPS = [
    'store.apps.StoreConfig',
    'nested_admin',
    'widget_tweaks',
    'crispy_forms',
    'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres'
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecom.urls'
X_FRAME_OPTIONS = 'SAMEORIGIN'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ecom.wsgi.application'
AUTH_USER_MODEL = 'store.User'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # previous was ->'postgres',->'ecom2'
        'NAME': os.environ.get("DJANGO_ECOM_DB_NAME"),
        'USER': os.environ.get("DJANGO_ECOM_DB_USER"),
        'PASSWORD': os.environ.get("DJANGO_ECOM_DB_PASSWORD"),
        'HOST': os.environ.get("DJANGO_ECOM_HOST"),
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    }
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
MESSAGE_LEVEL = messages.DEBUG

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_URL = '/handle_login/'

PAYTM_COMPANY_NAME = "MEERA STORE"   # For representation purposes
PAYTM_INDUSTRY_TYPE_ID = "Retail"     # For staging environment
PAYTM_CHANNEL_ID = "WEB"
PAYTM_MERCHANT_KEY = os.environ.get("DJANGO_ECOM_PAYTM_MERCHANT_KEY")
PAYTM_MERCHANT_ID = os.environ.get("DJANGO_ECOM_PAYTM_MERCHANT_ID")
PAYTM_CALLBACK_URL = "/response/"  # Hardcode
PAYTM_WEBSITE = "WEBSTAGING"
PAYTM_PAYMENT_GATEWAY_URL = "https://securegw-stage.paytm.in/order/process"
PAYTM_TRANSACTION_STATUS_URL = "https://securegw-stage.paytm.in/order/status"
SESSION_SAVE_EVERY_REQUEST = True
