"""
ASGI config for ai_portfolio_labs_base project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.settings')

application = get_asgi_application()
