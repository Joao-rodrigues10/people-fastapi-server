from pymongo import MongoClient
from src.config.core import EnvironmentCore, ENVIRONMENT_CORE
from src.domain.entities.people import PeopleEntity
from src.domain.interface.repositories.people_repository import IPeopleRepository


class PeopleRepositoryMongo(IPeopleRepository):
    def __init__(self, table: str, collection: str):
        self.environment: EnvironmentCore = ENVIRONMENT_CORE
        self.client = MongoClient(
            host=self.environment.mongo_host,
            port=self.environment.mongo_port,
            username=self.environment.mongo_user,
            password=self.environment.mongo_password.get_secret_value(),
            authSource="admin"
        )

        self.db = self.client[table]
        self.collection = self.db[collection]

    def create(self, people_entity: PeopleEntity) -> PeopleEntity | None:
        entity_data = people_entity.model_dump(exclude_none=True, by_alias=True)
        result = self.collection.insert_one(entity_data)

        if not result:
            return None

        return people_entity

    def get(self, people_id: str) -> PeopleEntity | None:
        filter = {"_id": people_id}
        result = self.collection.find_one(filter)

        if not result:
            return None

        return PeopleEntity(**result)

    def delete(self) -> int:
        ...

    def update(self) -> int:
        ...
