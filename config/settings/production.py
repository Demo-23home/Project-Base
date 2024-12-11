from os import getenv, path
from dotenv import load_dotenv

from .base import *  # noqa
from .base import BASE_DIR


# Loading ENV file
local_env_file = path.join(BASE_DIR / ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)


# Django Production Server Settings
SECRET_KEY = getenv("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = []

ADMIN_URL = getenv("DJANGO_ADMIN_URL")

AMDINS = [("Zeyad Mohammed Salama", "zeyadslama23@gmail.com"),]
