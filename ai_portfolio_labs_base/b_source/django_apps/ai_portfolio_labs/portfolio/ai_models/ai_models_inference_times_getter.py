import pathlib
from pathlib import Path
import keras
import torch
import time
import numpy
from PIL import Image
from torchvision import transforms, models
from keras.src.applications.efficientnet import EfficientNetB7
from keras.src.applications.efficientnet_v2 import preprocess_input
from ai_portfolio_labs_base.resources.model_weights.tensorflow.resources_model_weights_tensorflow_folder_path_getter import \
    get_resources_model_weights_tensorflow_folder_path


def get_ai_models_inference_times(
        input_image_path: Path):
    if input_image_path is None:
        return \
            None, None

    pytorch_time = \
        __get_pytorch_model_prediction_time(
            input_image_path=input_image_path)

    tensorflow_time = \
        __get_keras_plus_tensorflow_model_prediction_time(
            input_image_path=input_image_path)

    if pytorch_time <= 0 or tensorflow_time <=0:
        return None, None

    return \
        pytorch_time, tensorflow_time


def __get_keras_plus_tensorflow_model_prediction_time(
        input_image_path: Path) \
        -> float:
    tensorflow_model_weights_folder_path = \
        get_resources_model_weights_tensorflow_folder_path()

    weights_file_path = \
        pathlib.Path(
            tensorflow_model_weights_folder_path / 'efficientnetb7.h5')

    model = \
        EfficientNetB7(
            weights=None)

    model.load_weights(
        weights_file_path.__str__())

    keras_image_object_instance = \
        keras.utils.load_img(
            input_image_path,
            target_size=(600, 600))

    keras_image_object_as_array = \
        keras.utils.img_to_array(
            img=keras_image_object_instance)

    keras_image_object_as_array = \
        numpy.expand_dims(
            a=keras_image_object_as_array,
            axis=0)

    keras_image_object_as_array = \
        preprocess_input(
            x=keras_image_object_as_array)

    start_time = \
        time.time()

    model.predict(
        keras_image_object_as_array)

    tensorflow_time = (
            time.time() - start_time)

    return \
        tensorflow_time


def __get_pytorch_model_prediction_time(
        input_image_path: Path) \
        -> float:
    pytorch_model = \
        models.mobilenet_v2(
            weights='IMAGENET1K_V1')
    
    pytorch_model.eval()

    pytorch_model.cpu()

    pil_image_object_instance = \
        Image.open(
            input_image_path).convert('RGB')

    transform = \
        transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

    pytorch_input = \
        transform(pil_image_object_instance).unsqueeze(0)

    start_time = \
        time.time()

    with torch.no_grad():
        pytorch_model(
            pytorch_input)

    pytorch_time = \
        time.time() - start_time

    return \
        pytorch_time
