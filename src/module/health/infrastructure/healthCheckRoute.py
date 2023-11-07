
from common.enum.httpMethods import HttpMethods
from common.enum.httpStatusCode import HttpStatusCode
from common.router.abstractRouterConfigurator import AbstractRouterConfigurator
from common.router.router import Router
from module.health.infrastructure.controller.healthCheckController import HealthCheckController


class HealthCheckRoute(AbstractRouterConfigurator):
    def __init__(self, prefix: str) -> None:
        super().__init__(prefix)

    def set_handles(self):
        
        self.routers = [
            Router(
                path='/',
                method=HttpMethods.GET,
                controller=HealthCheckController(),
            )
        ]


healtCheckRoute = HealthCheckRoute('__healthCheck')