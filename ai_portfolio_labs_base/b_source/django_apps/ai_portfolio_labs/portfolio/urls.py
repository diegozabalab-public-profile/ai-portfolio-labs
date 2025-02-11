from django.urls import path
from ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.portfolio import landing_page_home


urlpatterns = [
    path('portfolio/', landing_page_home.landing_page_home, name='landing_page_home'),
]
