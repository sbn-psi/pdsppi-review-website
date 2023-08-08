"""
WSGI config for review project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

ENV = os.getenv("ENV")

if ENV == 'production':
	print('load production settings')
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "review.settings.production")
else:
	print('load development settings')
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "review.settings.dev")

application = get_wsgi_application()