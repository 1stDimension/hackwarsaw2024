from fastapi import HTTPException
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
  

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table
from sqlalchemy.orm import relationship, Mapped

association_table = Table(
    "association_table",
    BaseSQL.metadata,
    Column("voter_id", ForeignKey("users.id")),
    Column("meeting_id", ForeignKey("transcripts.id")),
)

class Meeting(BaseSQL):
    __tablename__ = "transcripts"
    id = Column(Integer, primary_key=True)
    transcript = Column(String,nullable=True)
    participants : Mapped[list["User"]]= relationship(secondary=association_table, back_populates="meetings")

class User(BaseSQL):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=uuid4)
    first_name = Column(String)
    last_name = Column(String)
    local = Column(String)
    meetings: Mapped[list[Meeting]] = relationship(secondary=association_table, back_populates="participants")

# class Presence(BaseSQL):
    # __tablename__ = "presences"
    # id = Column(Integer, primary_key=True)
    # meeting_id = Column(Integer,ForeignKey("transcript.id"))
    # meetings = relationship("transcripts    ")
    # voter_id = Column(Integer, ForeignKey("users.id"))
    # voters = relationship("User",back_populates="meetings")



F = Faker()
vs: list[Voter] = list()

BaseSQL.metadata.create_all(bind=engine)

M = Meeting()
print(M)

with SessionLocal() as sess:
    for i in range(10):
        v = Voter(
        first_name=F.name_female() if i % 2 == 0 else F.name_male(),
        last_name=F.last_name_female() if i % 2 == 0 else F.last_name_female(),
        local=F.building_number() 
        )
        u = User(first_name=v.first_name,last_name=v.last_name,local=v.local)
        sess.add(u)
        vs.append(v)
with SessionLocal() as sess:
    l = sess.query(User).all()
    print(l)

@app.get("/")
def read_main():
    list_voters = Voters(voters=vs)
    return list_voters

@app.post("/{voter_id}/absent")
def absent(voter_id: UUID):
    with SessionLocal() as sess:
        user = sess.query(User).filter(User.id == voter_id).first()
        if user:
            user.meetings.remove(M)
        else:
            raise HTTPException(404)
    

@app.post("/{voter_id}/present")
def present(voter_id: UUID):
    with SessionLocal() as sess:
        user = sess.query(User).filter(User.id == voter_id).first()
        if user:
            user.meetings.append(M)
            return User
        else:
            raise HTTPException(404)