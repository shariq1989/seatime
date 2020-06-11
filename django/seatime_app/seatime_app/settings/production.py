from seatime_app.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'Optional default value')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SERVER_IP = os.getenv('DJANGO_SERVER_IP', False)
if not SERVER_IP:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', SERVER_IP]

if not SERVER_IP:
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:8080'
    )
else:
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:8080', 'http://' + SERVER_IP, 'http://' + SERVER_IP + ':8000'
    )
