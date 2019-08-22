from mysite.settings.common import *

DEBUG = False

ALLOWED_HOSTS = ['18.179.78.15',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}