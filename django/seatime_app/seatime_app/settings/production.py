from seatime_app.settings.common import *
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'Optional default value')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '45.33.106.171', '127.0.0.1', 'warm-ocean-91075.herokuapp.com']

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080', 'http://45.33.106.171:8080', 'http://45.33.106.171'
)