from abc import ABC, abstractmethod
from application.models.country import Country
from flask import jsonify
from typing import List


from typing import TypeVar, Generic

T = TypeVar('T')


class BaseRepository(Generic[T], ABC):

    @abstractmethod
    def load(self) -> None:
        pass

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
    def get(self) -> List[T]:
        pass

    @abstractmethod
    def get_id(self, id) -> T:
        pass

