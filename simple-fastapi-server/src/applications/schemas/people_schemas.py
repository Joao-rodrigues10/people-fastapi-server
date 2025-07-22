from datetime import datetime

from pydantic import BaseModel, Field


class People(BaseModel):
    id: str | None = None
    name: str
    age: int
    birthdate: str | datetime
    last_name: str | None = None

def delete(self, user_id: str) -> bool:
    if user_id in self._db:
        del self._db[user_id]
        self._persist()
        return True
    return False

def update(self, user_id: str, new_data: People) -> People | None:
    if user_id in self._db:
        new_data.id = user_id
        self._db[user_id] = new_data.model_dump()
        self._persist()
        return new_data
    return None
