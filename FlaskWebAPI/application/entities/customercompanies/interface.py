from abc import ABC, abstractmethod
from application.entities.customercompanies.model import CustomerCompany
from typing import List


class BaseCustomerCompaniesRepository(ABC):
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
    def get(self) -> List[CustomerCompany]:
        pass

    @abstractmethod
    def get_id(self, id) -> CustomerCompany:
        pass

    