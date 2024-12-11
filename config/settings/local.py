from os import getenv, path
from dotenv import load_dotenv

from .base import * #noqa
from .base import BASE_DIR


# Loading ENV file
local_env_file  = path.join(BASE_DIR / ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)


# Django Local Server Settings
DEBUG = True

SITE_NAME = getenv("SITE_NAME")

SECRET_KEY = getenv("DJANGO_SECRET_KEY", "BVvesmQMhG4Z_uMopYUDRon6dZq6H_SP8FlKamyjtjBIGw4a9U0")

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

ADMIN_URL = getenv("DJANGO_ADMIN_URL")

# Email settings 
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = getenv("EMAIL_HOST")
EMAIL_PORT = getenv("EMAIL_PORT")
EMAIL_DEFAULT_FROM = getenv("DEFAULT_FROM_EMAIL")
DOMAIN = getenv("DOMAIN")