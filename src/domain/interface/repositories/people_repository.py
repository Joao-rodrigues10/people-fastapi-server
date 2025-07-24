from abc import ABC, abstractmethod

from src.domain.entities.people import PeopleEntity


class IPeopleRepository(ABC):

    @abstractmethod
    def create(self, people_entity: PeopleEntity) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get(self, people_id: str) -> PeopleEntity | None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self):
        raise NotImplementedError()

    @abstractmethod
    def update(self):
        raise NotImplementedError()