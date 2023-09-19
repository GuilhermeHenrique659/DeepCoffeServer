
from abc import ABC, abstractmethod

from flask import request, jsonify
from common.error.appError import AppError

class AbstractController(ABC):
    def __init__(self) -> None:
        super().__init__()

    def exec(self, payload):
        try:
            controller_output = self.handle(payload)
            return jsonify(controller_output)
        except Exception as error:
            print(error)
            raise AppError('Server internal error', 500)
        
    @abstractmethod
    def handle(self, data) -> any:
        pass