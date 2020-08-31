from abc import ABC, abstractmethod
from application.entities.employments.model import Employment
from typing import List


class BaseEmploymentsRepository(ABC):
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
    def get(self) -> List[Employment]:
        pass

    @abstractmethod
    def get_id(self, id) -> Employment:
        pass

    