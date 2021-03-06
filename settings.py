import os
from sc4py.env import env
URL_PATH_PREFIX = env("URL_PATH_PREFIX", "sead/id/")
os.environ.setdefault("URL_PATH_PREFIX", env("", "sead/id/"))
os.environ.setdefault("MY_APPS", "id")
os.environ.setdefault("POSTGRES_DB", env("POSTGRES_DB_ID"))

os.environ.setdefault("DJANGO_AUTH_USER_MODEL", "id.User")
os.environ.setdefault("DJANGO_LOGIN_URL", env("DJANGO_LOGIN_URL", '/%slogin/' % URL_PATH_PREFIX))
os.environ.setdefault("DJANGO_LOGOUT_URL", env("DJANGO_LOGOUT_URL", '/%slogout/' % URL_PATH_PREFIX))
os.environ.setdefault("DJANGO_LOGIN_REDIRECT_URL", env("DJANGO_LOGIN_REDIRECT_URL", '/%s' % URL_PATH_PREFIX))
os.environ.setdefault("DJANGO_LOGOUT_REDIRECT_URL", env("DJANGO_LOGOUT_REDIRECT_URL", '/%s' % URL_PATH_PREFIX))

from suap_ead.template_settings import *
