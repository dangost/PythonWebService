from abc import ABC, abstractmethod
from application.entities.countries.model import Country
from typing import List


class BaseCountriesRepository(ABC):
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
    def get(self) -> List[Country]:
        pass

    @abstractmethod
    def get_id(self, id) -> Country:
        pass

    