
from flask import Flask
from typing import List
from common.router.abstractRouterConfigurator import AbstractRouterConfigurator
from common.utils.loggerUtils import LoggerUtils
from config.envConfig import EnvConfig


class Application:
    __application: Flask
    __routes_configs: List[AbstractRouterConfigurator] = []

    def __init__(self, routers: List[AbstractRouterConfigurator]) -> None:
        self.__routes_configs = routers
        self.__application = Flask(__name__)

    def __setup_router(self):
        for router in self.__routes_configs:
            router.set_handles()
            router.setup_routes(self.__application)

    def create_app(self):
        return self.__application

    def setup(self):
        self.__setup_router()
        print(self.__application.url_map)
