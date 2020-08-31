from abc import ABC, abstractmethod
from application.entities.orderitems.model import OrderItem
from typing import List


class BaseOrderItemsRepository(ABC):
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
    def get(self) -> List[OrderItem]:
        pass

    @abstractmethod
    def get_id(self, id) -> OrderItem:
        pass

    