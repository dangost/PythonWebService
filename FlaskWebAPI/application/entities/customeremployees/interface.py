from abc import ABC, abstractmethod
from application.entities.customeremployees.model import CustomerEmployee
from typing import List


class BaseCustomerEmployeesRepository(ABC):
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
    def get(self) -> List[CustomerEmployee]:
        pass

    @abstractmethod
    def get_id(self, id) -> CustomerEmployee:
        pass

    