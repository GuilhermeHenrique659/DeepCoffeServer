from http import HTTPMethod
from common.model.model import convolutionalModel
from common.router.abstractRouterConfigurator import AbstractRouterConfigurator
from common.router.router import Router
from module.classifeirModel.infrastructure.controller.classifeirController import ClassifeirController
from module.classifeirModel.infrastructure.validation.classifeirValidation import ClassifeirValidation

class ClassifeirRoutes(AbstractRouterConfigurator):
    def __init__(self, prefix: str) -> None:
        super().__init__(prefix)
        self.validation = ClassifeirValidation()

    def set_handles(self):

        self.routers = [
            Router(
                path='/',
                controller=ClassifeirController(model=convolutionalModel),
                method=HTTPMethod.POST,
                validation=self.validation.validate_image()
            )
        ]


classifeirRoutes = ClassifeirRoutes('classifeir')