from seatime_app.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
try:
    from .secret_key import SECRET_KEY
except ImportError:
    SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
    generate_secret_key(os.path.join(SETTINGS_DIR, 'secret_key.py'))
    from .secret_key import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '45.33.106.171']

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080', 'http://45.33.106.171:8080'
)