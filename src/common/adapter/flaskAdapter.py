
from flask import request
from common.error.appError import AppError
from common.error.validationError import AppValidationError
from common.middleware.absactractMiddlware import AbstractMiddleware
from common.middleware.validationMiddleware import ValidationMiddleware
from common.router.router import Router


class FlaskAdapter:
    def __init__(self, router: Router) -> None:
        self.controller = router.controller
        self.validation = router.validation

        self.__middlewares = { 
            'validation': ValidationMiddleware(),
        }

    def adapter(self, **args):
        payload = {
            **args,
            **request.args,
            **request.get_json()
        }

        try:
            self.__middlewares.get('validation').run(payload, self.validation)
            return self.controller.exec(payload)
        except AppValidationError as error:
            return error.get_error_details()
        except AppError as error:
            return error.get_error_details()
