from datetime import datetime

from pydantic import BaseModel, Field


class PeopleEntity(BaseModel):
    id: str | None = Field(None, alias="_id")
    name: str
    age: int
    birthdate: str | datetime
    last_name: str | None = None

    class Config:
        populate_by_name = True
