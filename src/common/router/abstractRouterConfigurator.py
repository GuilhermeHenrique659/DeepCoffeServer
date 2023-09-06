from abc import ABC, abstractmethod

from flask import Flask
from common.router.router import Router
from typing import List

class AbstractRouterConfigurator(ABC):
    def __init__(self, prefix: str) -> None:
        self.routers: List[Router] = []
        self.prefix = prefix

    @abstractmethod
    def set_handles(self):
        pass

    def setup_routes(self, application: Flask):
        for router in self.routers:
            application.add_url_rule(f'/api/{self.prefix}{router.path}', 
                                    view_func=router.controller.exec, 
                                    methods=[router.method])
