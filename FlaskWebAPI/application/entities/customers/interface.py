from abc import ABC, abstractmethod
from application.entities.customers.model import Customer
from typing import List


class BaseCustomersRepository(ABC):
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
    def get(self) -> List[Customer]:
        pass

    @abstractmethod
    def get_id(self, id) -> Customer:
        pass

    