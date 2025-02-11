from django.http import JsonResponse


def landing_page_home(
        request):
    return \
        JsonResponse(
            {"message": "Welcome to AI Portfolio Labs!", "status": "success"})
