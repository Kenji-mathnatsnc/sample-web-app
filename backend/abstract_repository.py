from abc import *

from pydantic import BaseModel


class IRepository(metaclass=ABCMeta):
    @abstractmethod
    def find(self, key):
        pass

    @abstractmethod
    def save(self, model: BaseModel):
        pass

    @abstractmethod
    def delete(self, key):
        pass
