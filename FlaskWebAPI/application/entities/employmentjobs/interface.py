from abc import ABC, abstractmethod
from application.entities.employmentjobs.model import EmploymentJobs
from typing import List


class BaseEmploymentJobsRepository(ABC):
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
    def get(self) -> List[EmploymentJobs]:
        pass

    @abstractmethod
    def get_id(self, id) -> EmploymentJobs:
        pass

    