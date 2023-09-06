from flask import jsonify

class AppError(Exception):
    def __init__(self, message: str, status = 400) -> None:
        super().__init__()
        self.message = message
        self.status = status

    def get_error_details(self):
        return jsonify({
            'message': self.message,
            'status': self.status
        })