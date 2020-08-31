from abc import ABC, abstractmethod
from application.entities.phonenumbers.model import PhoneNumber
from typing import List


class BasePhoneNumbersRepository(ABC):
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
    def get(self) -> List[PhoneNumber]:
        pass

    @abstractmethod
    def get_id(self, id) -> PhoneNumber:
        pass

    