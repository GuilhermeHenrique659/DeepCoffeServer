
from flask import Flask

from config.envConfig import EnvConfig


class Application:
    __application: Flask

    def __init__(self) -> None:
        self.__application = Flask(__name__)
    
    def get_app(self):
        return self.__application

    def run(self):
        self.__application.run(debug=True, port=EnvConfig.get_port(), host=EnvConfig.get_ip())
