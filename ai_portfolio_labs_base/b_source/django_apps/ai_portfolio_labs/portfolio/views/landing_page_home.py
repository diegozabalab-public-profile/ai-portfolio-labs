from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def landing_page_home_as_html(
        request):
    return \
        render(
            request,
            template_name='landing_page_home.html')


# TODO: new way to interact with React - to move here later
def landing_page_home_as_json(
        request):
    return \
        JsonResponse(
            {"message": "Welcome to AI Portfolio Labs!", "status": "success"})


def ai_models_inference_times_results_as_html(
        request):
    return \
        render(
            request, "ai_models_inference_times_results.html")

