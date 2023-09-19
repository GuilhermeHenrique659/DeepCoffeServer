from donttrust import DontTrust, Schema, ValidationError
from typing import Callable
from common.error.validationError import AppValidationError

from common.middleware.absactractMiddlware import AbstractMiddleware

class ValidationMiddleware(AbstractMiddleware):
    def run(self, payload: dict, trust: DontTrust = None) -> None:
        if not trust: return

        try:
            trust.validate(payload)
        except ValidationError as error:
            raise AppValidationError(error.message, error.field)