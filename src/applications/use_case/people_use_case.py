from fastapi import HTTPException

from src.applications.schemas.people_schemas import PeopleSchema
from src.domain.entities.people import PeopleEntity
from src.domain.services.people_service import PeopleService


class PeopleUseCase:

    def __init__(self, people_service: PeopleService):
        self.people_service = people_service


    def create(self, people_schema: PeopleSchema)-> PeopleSchema:
        entity = PeopleEntity(
            **people_schema.model_dump()
        )
        entity_response = self.people_service.create(entity)

        if not entity_response:
            raise HTTPException(status_code=500, detail="Internal Server Error")

        return PeopleSchema(
            **entity_response.model_dump()
        )


    def get(self, people_id: str) -> PeopleSchema:
        entity: PeopleEntity | None = self.people_service.get(people_id)

        if not entity:
            raise HTTPException(status_code=404, detail="Not found")

        return PeopleSchema(
            **entity.model_dump()
        )


    def delete(self):
        self.people_service.delete()


    def update(self):
        self.people_service.update()