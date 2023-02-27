from .base import *  # noqa
from .base import env  # noqa

SECRET_KEY = "y2Fsb6N9Mw4fNNgBeALsMvlTdgO3CkmyNcReZFjFiZDEBMDSVFDwxdiebMcr4ATZ"

TEST_RUNNER = "django.test.runner.DiscoverRunner"

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

TEMPLATES[0]["OPTIONS"]["debug"] = True  # type: ignore # noqa F405
