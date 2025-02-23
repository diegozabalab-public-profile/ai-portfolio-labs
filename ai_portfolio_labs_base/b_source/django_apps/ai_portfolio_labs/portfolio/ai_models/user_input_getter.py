import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.portfolio.ai_models.ai_models_inference_times_getter import \
    get_ai_models_inference_times
from ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.portfolio.ai_models.helpers.is_loaded_image_size_larger_than_5mb_checker import \
    is_loaded_image_size_larger_than_5mb
from ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.portfolio.helpers.input_image_object_path_getter import \
    get_input_image_object_path


@csrf_exempt
def get_ai_models_inference_times_comparison(
        request):
    if request.method != 'POST':
        return \
            JsonResponse({
                'error': 'This endpoint only accepts POST requests.'},
                status=405)

    try:
        input_image_path = \
            get_input_image_object_path(
                request=request)

        is_allowed_image_size = \
            is_loaded_image_size_larger_than_5mb(
                input_image_path=input_image_path)

        if is_allowed_image_size:
            return \
                JsonResponse({
                    'error': 'File size exceeds the 5MB limit.'},
                    status=400)

        pytorch_time, tensorflow_time = \
            get_ai_models_inference_times(
                input_image_path=input_image_path)

        if pytorch_time is None or tensorflow_time is None:
            return \
                JsonResponse({
                    'error': 'AI model inference failed.'},
                    status=500)

        return \
            JsonResponse({
                'pytorch_time': str(pytorch_time),
                'tensorflow_time': str(tensorflow_time),
                'winner': 'PyTorch' if pytorch_time < tensorflow_time else 'TensorFlow'})

    except Exception as e:
        return \
            JsonResponse({
                'error': str(e)},
                status=500)
