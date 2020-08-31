from abc import ABC, abstractmethod
from application.entities.products.model import Product
from typing import List


class BaseProductsRepository(ABC):
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
    def get(self) -> List[Product]:
        pass

    @abstractmethod
    def get_id(self, id) -> Product:
        pass

    