import torch
 
class DeviceConfig:
    @staticmethod
    def get_device():
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
