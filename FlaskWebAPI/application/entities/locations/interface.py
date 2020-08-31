from abc import ABC, abstractmethod
from application.entities.locations.model import Location
from typing import List


class BaseLocationsRepository(ABC):
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
    def get(self) -> List[Location]:
        pass

    @abstractmethod
    def get_id(self, id) -> Location:
        pass

    