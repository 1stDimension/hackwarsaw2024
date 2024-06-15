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
  

from sqlalchemy import  Column, ForeignKey, Integer, String,Table
from sqlalchemy.orm import relationship, Mapped

association_table = Table(
    "association_table",
    BaseSQL.metadata,
    Column("voter_id", ForeignKey("users.id")), # type: ignore
    Column("meeting_id", ForeignKey("transcripts.id")), # type: ignore
)

class Meeting(BaseSQL):
    __tablename__ = "transcripts"
    id = Column(Integer, primary_key=True)
    transcript = Column(String,nullable=True)
    participants : Mapped[list["User"]]= relationship(secondary=association_table, back_populates="meetings")

class User(BaseSQL):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda : uuid4().hex)
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

# with SessionLocal() as sess:
    # for i in range(10):
        # v = Voter(
        # first_name=F.name_female() if i % 2 == 0 else F.name_male(),
        # last_name=F.last_name_female() if i % 2 == 0 else F.last_name_female(),
        # local=F.building_number() 
        # )
        # u = User(first_name=v.first_name,last_name=v.last_name,local=v.local)
        # sess.add(u)
        # sess.commit()
        # vs.append(v)
with SessionLocal() as sess:
    l = sess.query(User).all()
    print(l)

@app.get("/")
def read_main():
    with SessionLocal() as sess:
        l = sess.query(User).all()
    s : list[Voter]= list()
    for i in l:
        s.append(
            Voter(
                first_name=i.first_name,
                last_name=i.last_name,
                local=i.local,
                id=i.id
            )
        )
    return s

@app.post("/{voter_id}/absent")
def absent(voter_id: UUID):
    with SessionLocal() as sess:
        user = sess.query(User).filter(User.id == voter_id).first()
        if user:
            user.meetings.remove(M)
        else:
            raise HTTPException(404)
    

@app.post("/{voter_id}/present")
def present(voter_id: str):
    with SessionLocal() as sess:
        print(voter_id)
        user = sess.query(User).filter(User.id == voter_id).first()
        all = sess.query(User).all()
        for i in all:
            s = "".join(voter_id.split("-"))
            if s is voter_id:
                print(f"Mam cię {i.first_name}, {i.id}")
            print(f"{i.first_name}, {i.id}, comp {s}: {voter_id}")
        print(user)
        if user:
            user.meetings.append(M)
            return User
        else:
            raise HTTPException(404)