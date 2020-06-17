from seatime_app.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'Optional default value')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['96.126.97.44']
CORS_ORIGIN_WHITELIST = (
        'http://localhost:8080', 'http://96.126.97.44:8080'
)
