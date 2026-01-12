from pathlib import Path
from .settings import *

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False
ALLOWED_HOSTS = ["staging.yourdomain.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "staging.sqlite3",
    }
}

STATIC_ROOT = BASE_DIR / "staticfiles"  # <<<<< Ithu mandatory for collectstatic
