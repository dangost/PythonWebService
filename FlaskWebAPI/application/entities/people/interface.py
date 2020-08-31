from abc import ABC, abstractmethod
from application.entities.people.model import Person
from typing import List


class BasePeopleRepository(ABC):
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
    def get(self) -> List[Person]:
        pass

    @abstractmethod
    def get_id(self, id) -> Person:
        pass

    