from .base import *
import dj_database_url

DEBUG = os.environ.get('DEBUG', False)
SECRET_KEY = os.environ.get('SECRET_KEY', False)

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600, ssl_require=True)

try:
    from .local import *
except ImportError:
    pass
