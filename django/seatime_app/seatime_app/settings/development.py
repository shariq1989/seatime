from seatime_app.settings.common import *
import os

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databs

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5acq0rca0mr73',
        'USER': 'utywwtzdjfqwdi',
        'PASSWORD': 'da5b1e5f9574c7c3a9d061a0a8162d6a08b33d77e4b455eee988e7222bd39eb9',
        'HOST': 'ec2-18-214-211-47.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1c*3djyuzul-oyp%3*+8z%(n^+(#nk+cs+)d6#9u+74l%#_&ev'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.0.109']

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080', 'http://192.168.0.109:8080'
)