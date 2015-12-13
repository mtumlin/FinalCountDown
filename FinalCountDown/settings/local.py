from FinalCountDown.settings.base import *

SECRET_KEY = '5@r=_szpl3e$15_)wc@3=2z^h02%@xul_r&f3g6d_uwa270yi+'

DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}