import os
from typing import Any


BASE_DIR = os.path.dirname(__file__)
SETTINGS_MODULE = "tests.django_settings"

INSTALLED_APPS = ("bootstrap_pagination",)

DATABASES: dict[str, Any] = {}
MIDDLEWARE_CLASSES = ()

ROOT_URLCONF = "tests.django_settings.urls"
SECRET_KEY = "secretkey"
SITE_ROOT = "."
USE_TZ = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = ()

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": TEMPLATE_DIRS,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [],
            "debug": TEMPLATE_DEBUG,
        },
    },
]

urls: list[Any] = []
