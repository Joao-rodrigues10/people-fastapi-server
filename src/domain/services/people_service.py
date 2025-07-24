from src.domain.entities.people import PeopleEntity
from src.infraestructure.repositories.people_repository import PeopleRepositoryMongo


class PeopleService:

    def __init__(self, people_repository: PeopleRepositoryMongo):
        self.people_repository = people_repository

    def create(self, entity: PeopleEntity) -> PeopleEntity | None:
        return self.people_repository.create(entity)

    def get(self, people_id: str) -> PeopleEntity | None:
        return self.people_repository.get(people_id)

    def delete(self):
        self.people_repository.delete()

    def update(self):
        self.people_repository.update()