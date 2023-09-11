from flask import render_template, request, jsonify
import torch
import torchvision.transforms as transforms
from PIL import Image
import logging
import torch
import torch.nn as nn

logger = logging.getLogger(__name__)

# Verifica se a GPU está disponível
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class ConvolutionalModel(nn.Module):
    def __init__(self, num_class = 5):
        super(ConvolutionalModel, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )

        self.avgpool = nn.AdaptiveAvgPool2d((6, 6))
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(128 * 6 * 6, 512),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(512, num_class),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x


convolutionalModel = ConvolutionalModel()
convolutionalModel.load_state_dict(torch.load('src/common/model/modelo.pth', map_location=torch.device('cpu')))
convolutionalModel.eval()


# define a rota da API para receber uma imagem
def predict():
    # verifica se o arquivo é uma imagem
    if 'image' not in request.files:
        response = {'error': 'No image uploaded.'}
        return jsonify(response), 400

    file = request.files['image']

    try:
        image = Image.open(file)
    except:
        response = {'error': 'Invalid image.'}
        return jsonify(response), 400

    # redimensiona a imagem para o tamanho que o modelo espera
    transform = transforms.Compose([
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image = transform(image).unsqueeze(0).to(device)

    # desativa o cálculo do gradiente para economizar memória
    with torch.no_grad():
        # faz a previsão usando o modelo de rede neural
        output = model(image)

    # converte a saída do modelo em uma probabilidade e obtém o índice da classe com a maior probabilidade
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    class_index = torch.argmax(probabilities).item()

    # retorna a previsão como um dicionário de respostas
    response = {'class': class_index}

    return jsonify(response)