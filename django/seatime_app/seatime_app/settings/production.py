from seatime_app.settings.common import *

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
        'NAME': 'd2kest6kdunkuj',
        'USER': 'sbyptxvmletdyt',
        'PASSWORD': '69d9cfd041db710853eda525a99bda6fc82b9f7f8a7508596f39dc7aafee34d1',
        'HOST': 'ec2-52-204-20-42.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'Optional default value')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['seatime.work', '96.126.97.44']
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080', 'http://96.126.97.44', 'https://96.126.97.44',
    'https://clever-hoover-e243f0.netlify.app', 'http://clever-hoover-e243f0.netlify.app', 'http://seatime.work',
    'https://seatime.work'
)
