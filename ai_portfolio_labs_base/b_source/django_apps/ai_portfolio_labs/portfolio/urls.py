from django.urls import path
from ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.portfolio import landing_page_home


urlpatterns = [
    path('', landing_page_home.landing_page_home_as_html, name='landing_page_home_as_html'),
    path('portfolio/', landing_page_home.landing_page_home_as_html, name='landing_page_home_as_html'),
    path('api/portfolio/', landing_page_home.landing_page_home_as_json, name='landing_page_home_as_json'),
]
