from ..common import *  # noqa: ignore=F405

import os

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.10.2/ref/settings/#databases

ALLOWED_HOSTS += ['cloudcv.us-west-2.elasticbeanstalk.com'] # noqa

ADMINS = [('Admin', 'admin@cloudcv.org')]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    'cloudcv.org',
    'cloudcvbucket.s3.amazonaws.com',
    'cloudcv.us-west-2.elasticbeanstalk.com'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('RDS_DB_NAME', ''),
        'USER': os.environ.get('RDS_USERNAME', ''),
        'PASSWORD': os.environ.get('RDS_PASSWORD', ''),
        'HOST': os.environ.get('RDS_HOSTNAME', ''),
        'PORT': os.environ.get('RDS_PORT', ''),
    }
}

AWS_STORAGE_BUCKET_NAME = 'cloudcvbucket'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')

# Amazon S3 Configurations
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# static files configuration on S3
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'settings.prod.custom_storages.StaticStorage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# Media files configuration on S3
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'settings.prod.custom_storages.MediaStorage'

# Setup Email Backend related settings
DEFAULT_FROM_EMAIL = 'noreply@cloudcv.org'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '')

# Port number for the python-memcached cache backend.
CACHES['default']['LOCATION'] = os.environ.get('MEMCACHED_LOCATION', '127.0.0.1:11211') # noqa: ignore=F405

# https://docs.djangoproject.com/en/1.10/ref/settings/#secure-proxy-ssl-header
