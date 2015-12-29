from config.settings_base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'to^m7112x8gi0+05(vde#b2!sl*j_s9qyjx_&mht1okt0h_$^w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Email configuration
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_HOST = ''
#EMAIL_PORT = 587
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
