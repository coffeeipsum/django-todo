"""
WSGI config for django_todo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# That's the default
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-todo.settings")

# That's recommended by https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
os.environ["DJANGO_SETTINGS_MODULE"] = "django_todo.settings"

application = get_wsgi_application()
