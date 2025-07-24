from fastapi import APIRouter

from src.applications.schemas.people_schemas import PeopleSchema
from src.applications.use_case.people_use_case import PeopleUseCase
from src.domain.services.people_service import PeopleService
from src.infraestructure.repositories.people_repository import PeopleRepositoryMongo

router_app = APIRouter()

use_case = PeopleUseCase(
    people_service=PeopleService(people_repository=PeopleRepositoryMongo("people_table", "people_data")),
)

@router_app.get("/people/{user_id}")
def get(user_id: str):
    person = use_case.get(user_id)

    return person

@router_app.post("/people")
def create(request: PeopleSchema):
    person = use_case.create(request)

    return person
