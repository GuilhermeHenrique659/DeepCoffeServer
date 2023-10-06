from common.model.model import convolutionalModel
from common.router.abstractRouterConfigurator import AbstractRouterConfigurator
from common.router.router import Router
from module.classifeirModel.infrastructure.controller.classifeirController import ClassifeirController
from module.classifeirModel.infrastructure.validation.classifeirValidation import ClassifeirValidation
from common.enum.httpMethods import HttpMethods

class ClassifeirRoutes(AbstractRouterConfigurator):
    def __init__(self, prefix: str) -> None:
        super().__init__(prefix)
        self.validation = ClassifeirValidation()

    def set_handles(self):

        self.routers = [
            Router(
                path='/',
                controller=ClassifeirController(model=convolutionalModel),
                method=HttpMethods.POST,
                validation=self.validation.validate_image()
            )
        ]


classifeirRoutes = ClassifeirRoutes('classifeir')