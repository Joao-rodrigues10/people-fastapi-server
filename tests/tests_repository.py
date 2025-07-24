import uuid

import pytest

from src.domain.entities.people import PeopleEntity
from src.infraestructure.repositories.people_repository import PeopleRepositoryMongo

@pytest.fixture(scope="module")
def repository_db():
    return PeopleRepositoryMongo("people_table", "people_data")


def test_repository_get(repository_db):
    result = repository_db.get("d77096b4-8720-4796-835a-f115db6b539f")

    assert isinstance(result, PeopleEntity)

    assert result.name == "luiz"
    assert result.age == 25
    assert result.birthdate == "20/12/2000"
    assert result.last_name == "Rodrigues"

