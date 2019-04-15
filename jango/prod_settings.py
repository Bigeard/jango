import dj_database_url
from jango.settings import *

DATABASES['default'] = dj_database_url.config()

DEBUG = False
TEMPLATES_DEBUG = False

SECRET_KEY = get_env_variable('SECRET_KEY', '')

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ['app-jango.herokuapp.com']