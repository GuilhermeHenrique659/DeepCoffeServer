
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
            transforms.ToTensor(),
            transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616)),
            transforms.Resize((64, 64))
        ])

        image = transform(image).unsqueeze(0)  # Adicionar uma dimensão para representar o lote (batch)

        self.__model.eval()  # Coloque o modelo no modo de avaliação
        with torch.no_grad():
            image = image.to(DeviceConfig.get_device())  # Certifique-se de mover a imagem para a mesma GPU/Dispositivo que o modelo, se aplicável
            outputs = self.__model(image)
            probabilities = torch.softmax(outputs, dim=1)

        # As probabilidades contêm a probabilidade de cada classe
        class_probabilities = probabilities[0].cpu().numpy()  # Converte para NumPy
        CATEGORIES = ['Cerscospora','Healthy','Leaf rust','Miner','Phoma']

        response = []
        for class_idx, class_prob in enumerate(class_probabilities):
            class_name = CATEGORIES[class_idx]  # Substitua com suas próprias classes
            response.append({
                'Classe': class_name,
                'Probabilidade': f'{class_prob:.4f}'
            })
        
        return response