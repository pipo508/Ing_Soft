from abc import abstractmethod, ABC
from app import db

class Create(ABC):
    @abstractmethod
    def create(self, entity:db.Model):
        pass

