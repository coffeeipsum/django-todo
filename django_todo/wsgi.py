"""
WSGI config for django_todo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


# 1. That's the default
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-todo.settings")


# 2. That's recommended by https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
# os.environ["DJANGO_SETTINGS_MODULE"] = "django_todo.settings"


# 3. Found on StackOverflow
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")


application = get_wsgi_application()
