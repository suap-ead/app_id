"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import os
from sc4py.env import env
URL_PATH_PREFIX = env("URL_PATH_PREFIX", "ege/acesso/")
os.environ.setdefault("URL_PATH_PREFIX", env("", "ege/acesso/"))
os.environ.setdefault("MY_APPS", "ege_acesso")
os.environ.setdefault("POSTGRES_DB", env("POSTGRES_DB_ACESSO"))

os.environ.setdefault("DJANGO_AUTH_USER_MODEL", "ege_acesso.User")
os.environ.setdefault("DJANGO_LOGIN_URL", env("DJANGO_LOGIN_URL", '/%slogin/' % URL_PATH_PREFIX))
os.environ.setdefault("DJANGO_LOGOUT_URL", env("DJANGO_LOGOUT_URL", '/%slogout/' % URL_PATH_PREFIX))
os.environ.setdefault("DJANGO_LOGIN_REDIRECT_URL", env("DJANGO_LOGIN_REDIRECT_URL", '/%s' % URL_PATH_PREFIX))
os.environ.setdefault("DJANGO_LOGOUT_REDIRECT_URL", env("DJANGO_LOGOUT_REDIRECT_URL", '/%s' % URL_PATH_PREFIX))

from ege_utils.template_settings import *

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}, },
    'loggers': {
        '': {'handlers': ['console'], 'level': 'DEBUG'},
        'parso': {'handlers': ['console'], 'level': 'INFO'},
    },
}
