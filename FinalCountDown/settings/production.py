from FinalCountDown.settings.base import *
import dj_database_url

SECRET_KEY = '5@r=_szpl3e$15_)wc@3=2z^h02%@xul_r&f3g6d_uwa270yi+'

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']