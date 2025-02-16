import os
import pathlib
from ai_portfolio_labs_base.b_source.django_apps.ai_portfolio_labs.settings import MEDIA_ROOT_FOLDER_PATH
from ai_portfolio_labs_base.tests.common.inputs.jpgs.tests_common_inputs_jpgs_folder_path_getter import \
    get_tests_common_inputs_jpgs_folder_path


def get_input_image_object_path(
        request) \
        -> pathlib.Path:
    if 'image' in request.FILES:
        image_file = \
            request.FILES['image']

        file_name = \
            image_file.name

        media_uploads_folder_path = \
            pathlib.Path(MEDIA_ROOT_FOLDER_PATH) / 'uploads'

        media_uploads_folder_path.mkdir(
            parents=True,
            exist_ok=True)

        loaded_test_image_path = \
            media_uploads_folder_path / file_name

        with open(loaded_test_image_path, "wb") as f:
            f.write(
                image_file.read())

        return \
            loaded_test_image_path

    else:
        jpgs_folder_path = \
            get_tests_common_inputs_jpgs_folder_path()

        test_image_path = \
            pathlib.Path(jpgs_folder_path / 'cat.jpg')

        if not os.path.exists(test_image_path.__str__()):
            return \
                None

        return \
            test_image_path
