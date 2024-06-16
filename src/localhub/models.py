from pydantic import BaseModel, Field
from uuid import uuid4


class User(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex)


class Voter(BaseModel):
    first_name: str
    last_name: str
    local: str
    id: str = Field(default_factory=lambda: uuid4().hex)


class Voters(BaseModel):
    voters: list[Voter]


class Login(BaseModel):
    username: str
    password: str


class BillFull(BaseModel):
    pass


class CreateBill(BaseModel):
    contents: str


class Bill(CreateBill):
    id: str = Field(default_factory=lambda: uuid4().hex)
