from common.controller.abstractController import AbstractController
from common.enum.httpMethods import HttpMethods
from common.enum.httpStatusCode import HttpStatusCode


class Router:
    def __init__(self, path: str, 
                controller: AbstractController, 
                method: HttpMethods, 
                response_code: HttpStatusCode = HttpStatusCode.SUCCESS) -> None:
        self.path = path
        self.controller = controller
        self.method = method
        self.reponse_code = response_code
