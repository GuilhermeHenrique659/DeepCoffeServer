import os
from dotenv import load_dotenv

load_dotenv()

class EnvConfig:
    @staticmethod
    def get_port() -> int:
        port = int(os.getenv('PORT'))
        if port:
            return port
        return 5000
    
    @staticmethod
    def get_ip() -> str:
        ip = os.getenv('IP')
        if ip:
            return ip
        return 'localhost'