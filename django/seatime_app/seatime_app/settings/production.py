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
        'NAME': 'd5acq0rca0mr73',
        'USER': 'utywwtzdjfqwdi',
        'PASSWORD': 'da5b1e5f9574c7c3a9d061a0a8162d6a08b33d77e4b455eee988e7222bd39eb9',
        'HOST': 'ec2-18-214-211-47.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'Optional default value')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_WHITELIST = (
        'http://localhost:8080', 'http://96.126.97.44:8080', 'https://clever-hoover-e243f0.netlify.app', 'http://clever-hoover-e243f0.netlify.app', 'http://seatime.work'
)
