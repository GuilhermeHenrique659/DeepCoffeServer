from flask import jsonify

class AppValidationError(Exception):
    def __init__(self, message: str, context: str, status = 400) -> None:
        super().__init__()
        self.message = message
        self.status = status
        self.context = context

    def get_error_details(self):
        return jsonify({
            'message': self.message,
            'context': self.context,
            'status': self.status
        })