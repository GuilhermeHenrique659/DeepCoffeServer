from abc import ABC, abstractmethod

from flask import request


class AbstractMiddleware(ABC):
    @abstractmethod
    def run(self, agrs):
        pass