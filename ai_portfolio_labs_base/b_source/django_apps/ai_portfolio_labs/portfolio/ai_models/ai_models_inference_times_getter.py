from pathlib import Path
from ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.portfolio.ai_models.helpers.keras_plus_tensorflow_model_prediction_time_getter import \
    get_keras_plus_tensorflow_model_prediction_time
from ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.portfolio.ai_models.helpers.pytorch_model_prediction_time_getter import \
    get_pytorch_model_prediction_time


def get_ai_models_inference_times(
        input_image_path: Path) \
        -> tuple:
    if input_image_path is None:
        return \
            None, None

    pytorch_time = \
        get_pytorch_model_prediction_time(
            input_image_path=input_image_path)

    tensorflow_time = \
        get_keras_plus_tensorflow_model_prediction_time(
            input_image_path=input_image_path)

    if pytorch_time <= 0 or tensorflow_time <=0:
        return None, None

    return \
        pytorch_time, tensorflow_time
