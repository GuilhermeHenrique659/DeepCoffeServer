
import torch
from common.controller.abstractController import AbstractController
from common.model.model import ConvolutionalModel
import torchvision.transforms as transforms
from PIL import Image
from io import BytesIO
import base64
from config.deviceConfig import DeviceConfig

class ClassifeirController(AbstractController):
    def __init__(self, model: ConvolutionalModel) -> None:
        self.__model = model

    def handle(self, data) -> any:
        image = Image.open(BytesIO(base64.b64decode(data['image'])))

        transform = transforms.Compose([
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        image = transform(image).unsqueeze(0).to(DeviceConfig.get_device())

        with torch.no_grad():
            output = self.__model(image)

        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        class_index = torch.argmax(probabilities).item()

        response = {'class': class_index}

        return response