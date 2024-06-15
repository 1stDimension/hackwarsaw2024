from dataclasses import dataclass, field
from fastapi import HTTPException, Response
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from faker import Faker
from fastapi import FastAPI

app = FastAPI()


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BaseSQL = declarative_base()


class Voter(BaseModel):
    first_name: str
    last_name: str
    local: str
    id: UUID = Field(default_factory=uuid4)

class Voters(BaseModel):
    voters: list[Voter]
  
# class Presnet(BaseSQL):
    # __tablename__ = "presence"



F = Faker()
vs: list[Voter] = list()
for i in range(10):
    v = Voter(
    first_name=F.name_female() if i % 2 == 0 else F.name_male(),
    last_name=F.last_name_female() if i % 2 == 0 else F.last_name_female(),
    local=F.building_number() 
    )
    vs.append(v)

@app.get("/")
def read_main():
    list_voters = Voters(voters=vs)
    return list_voters

@app.post("/{voter_id}/absent")
def absent(voter_id: UUID):
    raise HTTPException(501)

@app.post("/{voter_id}/present")
def present(voter_id: UUID):
    raise HTTPException(501)