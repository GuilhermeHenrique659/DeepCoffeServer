from common.controller.abstractController import AbstractController
from common.enum.httpMethods import HttpMethods
from common.enum.httpStatusCode import HttpStatusCode
from donttrust import DontTrust


class Router:
    def __init__(self, path: str, 
                controller: AbstractController, 
                method: HttpMethods, 
                response_code: HttpStatusCode = HttpStatusCode.SUCCESS,
                validation: DontTrust = None) -> None:
        self.path = path
        self.controller = controller
        self.method = method
        self.reponse_code = response_code
        self.validation = validation
