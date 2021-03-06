from django.conf import settings
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*1wvt%2rb%1=hh5*8(kwlc2d-72wyp0n#%p#6yg_@1!!f#m%kb'
# SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'blog.apps.BlogConfig',
    'tracker.apps.TrackerConfig',
    'reaction.apps.ReactionConfig',
    'accounts.apps.AccountsConfig',
    'player.apps.PlayerConfig',
    'chat.apps.ChatConfig',
    'core',
    'amazon_store',
    'real_estate',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'storages',
    'social_django',  # I already install social-auth-app-django
    # 'widget_tweaks',  # for chat app
    # 'rest_framework',  # for chat app

    'ckeditor',
    'ckeditor_uploader',
    'embed_video',

    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
]
CKEDITOR_UPLOAD_PATH = "document/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': 'auto',
        "removePlugins": "stylesheetparser",

    },
}
AWS_QUERYSTRING_AUTH = True


INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # below are third party for social login effect
    'social_django.middleware.SocialAuthExceptionMiddleware',

    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'application.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # neccessay for allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Below were added for social login
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

                'django.template.context_processors.media',
            ],
        },
    },
]
# Below is also for the social login auth
AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    # For allauth
    # 'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
]
# SITE_ID = 1

WSGI_APPLICATION = 'application.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'worldgist_database',
        'USER': 'postgres',
        'PASSWORD': 'chibles247',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
# AWS_S3_REGION_NAME = "ap-south-1"
AWS_S3_REGION_NAME = 'us-east-2'
AWS_S3_SIGNATURE_VERSION = "s3v4"

# FOR THE REMEMBER ME CHECKBOX
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'myworldgist@gmail.com'
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER_WORLDGIST')
EMAIL_HOST_PASSWORD = 'dmsexlijvokftvcz'
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD_WORLDGIST')
DEFAULT_EMAIL_FROM = 'myworldgist.com'

# For the social login
LOGIN_URL = 'accounts/login/'
LOGOUT_URL = 'accounts/logout/'
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '2824257444468967'
SOCIAL_AUTH_FACEBOOK_SECRET = '98d39eab009794789c5a8ed79ae96238'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '449947140519-ju7jjjgdsu0u08uiokd41msdcofv1ka2.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'd6_9LrFkooGW5HAtaudDlaa-'
