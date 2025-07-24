import json
import os
import uuid
from typing import Any

from fastapi import APIRouter, HTTPException

from src.applications.schemas.people_schemas import People
router_app = APIRouter()
PEOPLE_PATH = "database.json"

class PeopleDatabase:
    def __init__(self):
        if not os.path.exists(PEOPLE_PATH):
            with open(PEOPLE_PATH, "w") as f:
                json.dump({}, f)

        with open(PEOPLE_PATH, "r") as f:
            self._db: dict[str, Any] = json.load(f)

    def get(self, user_id: str) -> People | None:
        people = self._db.get(user_id)

        if people:
            return People(**people)

        return None


    def add(self, person: People):
        person.id = str(uuid.uuid4())
        self._db[person.id] = person.model_dump()
        self._persist()

        return person


    def _persist(self):
        with open(PEOPLE_PATH, "w") as f:
            json.dump(self._db, f, indent=2)


people_db = PeopleDatabase()


@router_app.get("/people/{user_id}")
def server(user_id: str):
    person = people_db.get(user_id)

    if person:
        return person

    raise HTTPException(status_code=404, detail="People not found")


@router_app.post("/people")
def server_post(request: People):
    person = people_db.add(request)

    if person:
        return person

    raise HTTPException(status_code=500, detail="Internal Server Error")

@router_app.delete("/people/{user_id}")
def delete_person(user_id: str):
    success = people_db.delete(user_id)
    if success:
        return {"message": "Pessoa deletada com sucesso"}
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")

@router_app.put("/people/{user_id}")
def update_person(user_id: str, updated: People):
    person = people_db.update(user_id, updated)
    if person:
        return person
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")