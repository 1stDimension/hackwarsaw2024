from datetime import datetime
from uuid import uuid4

from faker import Faker
from sqlalchemy import Column, ForeignKey, Integer, String, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, relationship, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BaseSQL = declarative_base()

association_table = Table(
    "association_table",
    BaseSQL.metadata,
    Column("voter_id", ForeignKey("users.id")),  # type: ignore
    Column("meeting_id", ForeignKey("transcripts.id")),  # type: ignore
)


class Meeting(BaseSQL):
    __tablename__ = "transcripts"
    id = Column(Integer, primary_key=True)
    transcript = Column(String, nullable=True)
    participants: Mapped[list["User"]] = relationship(
        secondary=association_table, back_populates="meetings"
    )


class User(BaseSQL):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: uuid4().hex)
    first_name = Column(String)
    last_name = Column(String)
    local = Column(String)
    meetings: Mapped[list[Meeting]] = relationship(
        secondary=association_table, back_populates="participants"
    )


BaseSQL.metadata.create_all(bind=engine)


class Bill(BaseSQL):
    __tablename__ = "bills"
    id = Column(String, primary_key=True, default=lambda: uuid4().hex)
    contents = Column(String, nullable=False)
    creation_date = Column(String, default=lambda: datetime.now().timestamp)


def init_db():
    F = Faker()
    with SessionLocal() as sess:
        for i in range(10):
            v = User(
                first_name=F.name_female() if i % 2 == 0 else F.name_male(),
                last_name=F.last_name_female() if i % 2 == 0 else F.last_name_female(),
                local=F.building_number(),
            )
            sess.add(v)
            sess.commit()
    with SessionLocal() as sess:
        return sess.query(User).all()
