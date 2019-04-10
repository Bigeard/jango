import dj_database_url
from jango.settings import *

DATABASES['default'] = dj_database_url.config()

DEBUG = False
TEMPLATES_DEBUG = False

ALLOWED_HOSTS = ['app-jango.herokuapp.com']

SECRET_KEY = get_env_variable('SECRET_KEY', '')