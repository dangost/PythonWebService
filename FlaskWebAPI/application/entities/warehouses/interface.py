from abc import ABC, abstractmethod
from application.entities.warehouses.model import Warehouse
from typing import List


class BaseWarehousesRepository(ABC):
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
    def get(self) -> List[Warehouse]:
        pass

    @abstractmethod
    def get_id(self, id) -> Warehouse:
        pass

    