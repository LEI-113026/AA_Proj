from abc import ABC, abstractmethod

class IObject(ABC):
    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def get_symbol(self):
        pass

    @abstractmethod
    def _check_self(self):
        pass