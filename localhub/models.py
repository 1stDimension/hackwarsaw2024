from pydantic import BaseModel, Field
from uuid import uuid4


class User(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)
