from abc import ABC, abstractmethod
from application.entities.restrictedinfo.model import RestrictedInfo
from typing import List


class BaseRestrictedInfoRepository(ABC):
    @abstractmethod
    def add(self, obj) -> None:
        pass

    @abstractmethod
    def edit(self, id, obj) -> None:
        pass

    @abstractmethod
    def delete(self, id) -> None:
        pass

    @abstractmethod
    def get(self) -> List[RestrictedInfo]:
        pass

    @abstractmethod
    def get_id(self, id) -> RestrictedInfo:
        pass

    