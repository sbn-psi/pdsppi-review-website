"""
Django settings for review project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# Application definition
INSTALLED_APPS = [
    'home',
    'search',
    'userauth',
    'missions',
    'django_comments_xtd',
    'django_comments',
    'storages',
    'seed',

    'wagtail.contrib.forms',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.redirects',
    'wagtail.contrib.settings',
    'wagtail.contrib.table_block',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'widget_tweaks',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'review.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
            os.path.join(BASE_DIR, 'userauth/templates/userauth'),
            os.path.join(BASE_DIR, 'missions/templates/comments'),
            os.path.join(BASE_DIR, 'missions/templates/django-comments-xtd'),
            os.path.join(BASE_DIR, 'missions/templates/missions'),
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

WSGI_APPLICATION = 'review.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_USER_MODEL = 'userauth.CustomUser'


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

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'America/Los_Angeles'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
    os.path.join(BASE_DIR, 'missions/static/missions'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.1/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Wagtail settings
WAGTAIL_SITE_NAME = "review"
WAGTAIL_FRONTEND_LOGIN_TEMPLATE='missions/login.html'
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = 'ckingston@psi.edu'
WAGTAILADMIN_NOTIFICATION_USE_HTML = True
WAGTAIL_ENABLE_UPDATE_CHECK = True
WAGTAIL_USER_CREATION_FORM = 'userauth.forms.WagtailUserCreationForm'
WAGTAIL_USER_EDIT_FORM = 'userauth.forms.WagtailUserEditForm'
WAGTAIL_USER_CUSTOM_FIELDS = ['display_name', 'addtl_info', 'photo',]
SITE_ID = 1

# Comments Settings
COMMENTS_APP = 'django_comments_xtd'
COMMENTS_XTD_SALT = (b"Timendi causa est nescire. "
                     b"Aequam memento rebus in arduis servare mentem.")
COMMENTS_XTD_FROM_EMAIL = "no-reply@igpp.ucla.edu"
COMMENTS_XTD_CONTACT_EMAIL = "ckingston@psi.edu"

COMMENTS_XTD_MODEL = 'missions.models.CustomComment'
COMMENTS_XTD_MAX_THREAD_LEVEL = 5
COMMENTS_XTD_LIST_ORDER = ('-thread_id', 'order')

CSRF_TRUSTED_ORIGINS = ['https://review-service.u4m6gudpq07vk.us-west-2.cs.amazonlightsail.com']

# AWS S3, Cloudflare CDN configuration
# stores/serves static and media directories in AWS in production
USE_S3 = os.getenv('DEBUG') == 'False'
print(f'DEBUG: {os.getenv("DEBUG")}')
print(f'USE_S3: {USE_S3}')

if USE_S3:
    # Upload media files to S3
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    # Using S3 as a CDN (via CloudFront), tell storage to serve files from there
    AWS_S3_CUSTOM_DOMAIN = 'd3qrohnnpazynl.cloudfront.net'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 static settings
    AWS_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    # Allow `django-admin collectstatic` to automatically put your static files in your bucket
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'
else:
    try:
        from .dev import *
    except ImportError:
        pass
