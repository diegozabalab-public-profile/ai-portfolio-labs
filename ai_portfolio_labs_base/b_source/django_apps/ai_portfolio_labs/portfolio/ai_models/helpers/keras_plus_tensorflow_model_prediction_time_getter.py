from pathlib import Path
import keras
import time
import numpy
from keras.src.applications.efficientnet import EfficientNetB7
from keras.src.applications.efficientnet_v2 import preprocess_input


def get_keras_plus_tensorflow_model_prediction_time(
        input_image_path: Path) \
        -> float:
    model = \
        EfficientNetB7(
            weights='imagenet')

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
