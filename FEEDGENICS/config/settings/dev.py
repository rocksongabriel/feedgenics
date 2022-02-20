from .base import *


SECRET_KEY = "=00qz-2zh*e5!0@c&&b9$ro+u)dot^f84d*0^4fbc)qg5(#n)7"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    "debug_toolbar",
]

SHELL_PLUS = "ipython"

# EMAIL CONFIGURATION FOR TESTING
DEFAULT_FROM_EMAIL = "test@feedgenics.com"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# DJANGO DEBUG TOOLBAR SETTINGS

MIDDLEWARE.insert(
    2,
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

INTERNAL_IPS = [
    "127.0.0.1",
]

def show_toolbar(request):
    return False

DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": show_toolbar}