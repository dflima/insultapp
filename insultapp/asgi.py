"""
ASGI config for insultapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application  # pylint: disable=import-error

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insultapp.settings')

application = get_asgi_application()
