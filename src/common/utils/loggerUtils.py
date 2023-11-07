from flask import current_app


class LoggerUtils:
    @staticmethod
    def info(txt: str):
        current_app.logger.info(txt)

    @staticmethod
    def error(txt: str):
        current_app.logger.error(txt)

    @staticmethod
    def warn(txt: str):
        current_app.logger.warn(txt)