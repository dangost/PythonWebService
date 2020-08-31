from abc import ABC, abstractmethod
from application.entities.orders.model import Orders
from typing import List


class BaseOrdersRepository(ABC):
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
    def get(self) -> List[Orders]:
        pass

    @abstractmethod
    def get_id(self, id) -> Orders:
        pass

    