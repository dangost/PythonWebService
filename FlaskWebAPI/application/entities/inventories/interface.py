from abc import ABC, abstractmethod
from application.entities.inventories.model import Inventory
from typing import List


class BaseInventoriesRepository(ABC):
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
    def get(self) -> List[Inventory]:
        pass

    @abstractmethod
    def get_id(self, id) -> Inventory:
        pass

    