import abc
from users.model import user_model

class Abstract(abc.ABC):

    @abc.abstractmethod
    def add(self, user: user_model.User):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get(self, reference) -> user_model.User:
        raise NotImplementedError
