import torch
import logging
import torch
import torch.nn as nn
import os

# Obtém o diretório atual do código em execução
current_directory = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para o arquivo de modelo
modelo_path = os.path.join(current_directory, 'modelo.pth')

logger = logging.getLogger(__name__)

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
convolutionalModel.load_state_dict(torch.load(modelo_path, map_location=torch.device('cpu')))
convolutionalModel.eval()
