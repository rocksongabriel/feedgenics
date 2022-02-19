from .base import *


SECRET_KEY = "=00qz-2zh*e5!0@c&&b9$ro+u)dot^f84d*0^4fbc)qg5(#n)7"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += []

SHELL_PLUS = "ipython"

# EMAIL CONFIGURATION FOR TESTING
DEFAULT_FROM_EMAIL = "test@feedgenics.com"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'