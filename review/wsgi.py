"""
WSGI config for review project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

DEBUG = os.environ.get("DEBUG")

if DEBUG == 'True':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "review.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "review.settings.production")

application = get_wsgi_application()
