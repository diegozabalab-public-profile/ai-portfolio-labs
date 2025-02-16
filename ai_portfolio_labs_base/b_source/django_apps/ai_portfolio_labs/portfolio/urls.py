from django.urls import path
from ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.portfolio.views import landing_page_home
from ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.portfolio.ai_models.user_input_getter import \
    get_ai_models_inference_times_comparison


urlpatterns = [
    path('', landing_page_home.landing_page_home_as_html, name='landing_page_home_as_html'),
    path('ai_models_inference_times_results/', landing_page_home.ai_models_inference_times_results_as_html, name='ai_models_inference_times_results'),
    path('api/portfolio/', landing_page_home.landing_page_home_as_json, name='landing_page_home_as_json'),
    path('api/ai_models_inference_times_comparison/', get_ai_models_inference_times_comparison, name='ai_models_inference_times_comparison'),
]
