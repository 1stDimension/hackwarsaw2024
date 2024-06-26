"""
This type stub file was generated by pyright.
"""

from pydantic import BaseModel

class User(BaseModel):
    id: str = ...


class Voter(BaseModel):
    first_name: str
    last_name: str
    local: str
    id: str = ...


class Voters(BaseModel):
    voters: list[Voter]
    ...


class BillFull(BaseModel):
    ...


class Bill(BaseModel):
    ...


