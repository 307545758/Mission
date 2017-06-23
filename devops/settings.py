"""
Django settings for devops project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from config import env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ssh key path
SSH_KEY_DIR = BASE_DIR + '/keys/'

#log dir
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# URL
CURRENT_URL = env.get('base', 'url')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2fr894dw2d!e0i@$ut&2ys8+9nr5if(k!+fikqnm=l_4-g3r91'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["*"]

# Application definitioncd

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'devops',
    'apps',
    'common',
    'django_crontab',
    'markdown_deux',
    'DjangoUeditor',




]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middleware.auth.AuthMiddleware',
    'common.middleware.oplog.OperationLogMiddleware',
]

ROOT_URLCONF = 'devops.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),

        ],
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

WSGI_APPLICATION = 'devops.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.get('db', 'database'),
        'USER': env.get('db', 'user'),
        'PASSWORD': env.get('db', 'password'),
        'HOST': env.get('db', 'host'),
        'PORT': env.getint('db', 'port')
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR,"../static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


REDIS_HOST=env.get('redis','ip')
REDIS_PORT=env.get('redis','port')


CODE_PATH =  env.get('project','code_path')

GIT_IP = ["124.207.112.3","125.208.12.224"]


REDIS_HOST = env.get('redis','ip')
REDIS_PORT = env.get('redis','port')

USERNAME = env.get('user','username')

SSH_KEY = env.get('user','ssh_key_path')

# mail config
EMAIL_ENABLE = env.get('mail', 'email_host')
EMAIL_HOST = env.get('mail', 'email_host')
EMAIL_PORT = env.get('mail', 'email_port')
EMAIL_HOST_USER = env.get('mail', 'email_host_user')
EMAIL_HOST_PASSWORD = env.get('mail', 'email_host_password')
EMAIL_USE_TLS = env.getboolean('mail', 'email_use_tls')

CRONJOBS = [

    ('0 0 * * *', 'apps.cron.update_assets_info'),
]

LOG_LEVEL = env.get('logger', 'log')
QUEUE_KEY = "code_push_task"

