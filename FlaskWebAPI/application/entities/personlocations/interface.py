from abc import ABC, abstractmethod
from application.entities.personlocations.model import PersonLocation
from typing import List


class BasePersonLocationsRepository(ABC):
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
    def get(self) -> List[PersonLocation]:
        pass

    @abstractmethod
    def get_id(self, id) -> PersonLocation:
        pass

    