
from abc import ABC, abstractmethod

from flask import request, jsonify
from common.error.appError import AppError

class AbstractController(ABC):
    def __init__(self) -> None:
        super().__init__()

    def exec(self, **args):
        controller_input = {
            **args,
            **request.args,
            **request.get_json()
        }

        try:
            controller_output = self.handle(controller_input)
            return jsonify(controller_output)
        except AppError as error:
            return error.get_error_details()
        except Exception as error:
            print(error)
            return AppError('Server internal error', 500).get_error_details()
        
    @abstractmethod
    def handle(self, data) -> any:
        pass