
from abc import ABC, abstractmethod

from common.error.appError import AppError
from common.utils.loggerUtils import LoggerUtils

class AbstractController(ABC):
    def __init__(self) -> None:
        super().__init__()

    def get_controller_name(self):
        return self.__class__.__name__

    def exec(self, payload):
        try:
            LoggerUtils.info(f'Running controller: {self.__class__.__name__}')
            controller_output = self.handle(payload)
            return controller_output
        except Exception as error:
            LoggerUtils.error(error)
            raise AppError('Server internal error', 500)
        
    @abstractmethod
    def handle(self, data) -> any:
        pass