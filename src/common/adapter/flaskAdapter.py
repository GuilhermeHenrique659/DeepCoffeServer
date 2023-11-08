
from flask import jsonify, request
from flask.views import View
from common.error.appError import AppError
from common.error.validationError import AppValidationError
from common.middleware.absactractMiddlware import AbstractMiddleware
from common.middleware.validationMiddleware import ValidationMiddleware
from common.router.router import Router
from common.utils.loggerUtils import LoggerUtils


class FlaskAdapter(View):
    def __init__(self, router: Router) -> None:
        self.controller = router.controller
        self.validation = router.validation

        self.__middlewares = { 
            'validation': ValidationMiddleware(),
        }

    def dispatch_request(self, **args):
        LoggerUtils.info(f'Request headers: \n{request.headers}')
        payload = {
            **args,
            **request.args,
            **(request.get_json() if request.content_type == 'application/json' else {})
        }

        try:
            self.__middlewares.get('validation').run(payload, self.validation)

            response = self.controller.exec(payload)
            return jsonify({ 'data': response, 'url': request.base_url })
        except AppValidationError as error:
            LoggerUtils.error(f'Error: {error.message}')
            return error.get_error_details()
        except AppError as error:
            LoggerUtils.error(f'Error: {error.message}')
            return error.get_error_details()
