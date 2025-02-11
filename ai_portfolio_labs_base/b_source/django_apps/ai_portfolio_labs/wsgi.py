"""
WSGI config for ai_portfolio_labs_base project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.settings')

application = get_wsgi_application()
