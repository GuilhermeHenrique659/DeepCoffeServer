from common.controller.abstractController import AbstractController
from common.utils.loggerUtils import LoggerUtils

class HealthCheckController(AbstractController):
    def handle(self, data) -> any:
        LoggerUtils.info('Application is running')
        return {
            'application running': True
        }