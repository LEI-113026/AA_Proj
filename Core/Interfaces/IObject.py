from abc import ABC, abstractmethod

from Core.Models import ObjectInfo


class IObject(ABC):
    @abstractmethod
    def get_info(self) -> ObjectInfo:
        pass

    @abstractmethod
    def _check_self(self):
        pass