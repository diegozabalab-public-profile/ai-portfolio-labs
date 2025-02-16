import pathlib
import pytest
from ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.portfolio.ai_models.ai_models_inference_times_getter import \
    get_ai_models_inference_times
from ai_portfolio_labs_base.tests.common.inputs.jpgs.tests_common_inputs_jpgs_folder_path_getter import \
    get_tests_common_inputs_jpgs_folder_path


class TestAiModelsInferenceTimesGetter:
    def test_ai_models_inference_times_getter(
            self):
        tests_common_inputs_jpgs_folder_path = \
            get_tests_common_inputs_jpgs_folder_path()

        input_image_path = \
            pathlib.Path(
                tests_common_inputs_jpgs_folder_path / 'cat.jpg')

        pytorch_time, tensorflow_time = \
            get_ai_models_inference_times(
                input_image_path=input_image_path)

        if pytorch_time is None or tensorflow_time is None:
            pytest.fail(
                'Output values are empty.')
