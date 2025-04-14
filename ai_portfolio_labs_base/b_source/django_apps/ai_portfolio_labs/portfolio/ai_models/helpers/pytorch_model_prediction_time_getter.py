from pathlib import Path
import torch
import time
from PIL import Image
from torchvision import transforms, models


def get_pytorch_model_prediction_time(
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
        transform(
            pil_image_object_instance).unsqueeze(0)

    start_time = \
        time.time()

    with torch.no_grad():
        pytorch_model(
            pytorch_input)

    pytorch_time = \
        time.time() - start_time

    return \
        pytorch_time
