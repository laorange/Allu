"""
Django settings for DjangoProjectSettings project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from .secret import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Application definition
INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # tools
    'corsheaders',
    'django_filters',
    'import_export',
    'uuslug',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',

    # my app
    'index',
    'course',
]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# ALLOWED_HOSTS = ['.quoi.top']
# SESSION_COOKIE_DOMAIN = ".quoi.top"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS
    'django.middleware.common.CommonMiddleware',  # CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoProjectSettings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'DjangoProjectSettings.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 关闭国际时间，不然数据库报错

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# 静态文件收集
STATIC_URL = '/static/'
if not DEBUG:
    STATIC_ROOT = str(BASE_DIR / 'static')
else:
    STATICFILES_DIRS = [
        str(BASE_DIR / "static")
    ]

# 媒体文件收集
MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR / 'media')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '{levelname} {asctime} {module} process-{process:d} thread-{thread:d}: {message}\n',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'encoding': 'utf-8',
            'delay': True,
            # 'maxBytes': 1024,
            # 'backupCount': 20,
        },
        'mail_admins': {
            'level': 'ERROR',
            'formatter': 'standard',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'include_html': False,
        }
    },
    'loggers': {
        'django': {
            # 'handlers': ['console', "mail_admins"],
            'handlers': ['console', "file"],
            # 'handlers': ['console'],
            'propagate': True,
        }
    }
}

# drf settings
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',  # session认证
        'rest_framework.authentication.BasicAuthentication',  # 基本认证
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 20,

    # # 设置api访问限制
    # 'DEFAULT_THROTTLE_CLASSES': (
    #     'rest_framework.throttling.AnonRateThrottle',  # ip 匿名用户
    #     'rest_framework.throttling.UserRateThrottle'  # token(session)
    # ),
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '1/minute',
    #     'user': '50/second',
    # }
}

SIMPLEUI_LOGO = '/static/favicon.ico'
SIMPLEUI_HOME_INFO = False
# SIMPLEUI_HOME_PAGE = "/"

SECURE_SSL_REDIRECT = not DEBUG

LOGIN_URL = "/admin/login/"
