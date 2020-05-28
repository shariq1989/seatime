from seatime_app.settings.common import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1c*3djyuzul-oyp%3*+8z%(n^+(#nk+cs+)d6#9u+74l%#_&ev'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.0.109']

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080', 'http://192.168.0.109:8080'
)