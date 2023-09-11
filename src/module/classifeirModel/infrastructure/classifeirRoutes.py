from http import HTTPMethod
from common.model.model import convolutionalModel
from common.router.abstractRouterConfigurator import AbstractRouterConfigurator
from common.router.router import Router
from module.classifeirModel.infrastructure.controller.classifeirController import ClassifeirController

class ClassifeirRoutes(AbstractRouterConfigurator):
    def __init__(self, prefix: str) -> None:
        super().__init__(prefix)

    def set_handles(self):

        self.routers = [
            Router(
                path='/',
                controller=ClassifeirController(model=convolutionalModel),
                method=HTTPMethod.POST
            )
        ]


classifeirRoutes = ClassifeirRoutes('classifeir')