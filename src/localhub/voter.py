from fastapi import HTTPException
from fastapi import FastAPI
from localhub.models import Login, Voter, Voters, Vote  # type: ignore
from localhub.sql import Meeting, User, SessionLocal, VoteBase  # type: ignore

app = FastAPI()

M = Meeting()


@app.post("/")
def new_voter(voter: Voter):
    with SessionLocal() as s:
        new_voter = User(
            first_name=voter.first_name,
            last_name=voter.last_name,
            local=voter.local,
        )
        s.add(new_voter)
        s.commit()
        voter = s.refresh(new_voter)
        return voter


@app.post("/login")
def login_user(user: Login):
    with SessionLocal() as s:
        user = s.query(User).filter(
            User.username == user.username,
            User.password == user.password
        ).first()
        return user


@app.get("/")
def read_main():
    with SessionLocal() as sess:
        l = sess.query(User).all()

        s: list[Voter] = list()
        for i in l:
            s.append(
                Voter(
                    first_name=i.first_name,  # type: ignore
                    last_name=i.last_name,  # type: ignore
                    local=i.local,  # type: ignore
                    id=i.id  # type: ignore
                )
            )
    return s


@app.post("/{voter_id}/absent")
def absent(voter_id: str):
    with SessionLocal() as sess:
        user = sess.query(User).filter(User.id == voter_id).first()
        if user and M in user.meetings:
            user.meetings.remove(M)
        else:
            raise HTTPException(404)


@app.post("/{voter_id}/present")
def present(voter_id: str):
    with SessionLocal() as sess:
        print(voter_id)
        try:
            user = sess.query(User).filter(User.id == voter_id).first()
            # all = sess.query(User).all()
            # for i in all:
            # s = "".join(voter_id.split("-"))
            # if s is voter_id:
            # print(f"Mam cię {i.first_name}, {i.id}")
            # print(f"{i.first_name}, {i.id}, comp {s}: {voter_id}")
            # print(user)
            print("Found")
            if user:
                print("Appended")
                user.meetings.append(M)
                print("User")
                return Voter(
                    first_name=user.first_name,  # type: ignore
                    last_name=user.last_name,  # type: ignore
                    local=user.local,  # type: ignore
                    id=user.id  # type: ignore
                )
            else:
                raise HTTPException(404)
        except Exception as e:
            print(e)


@app.post("/vote/")
def voter_vote(vote: Vote):
    with SessionLocal() as s:
        vote_base = VoteBase(**vote.dict())
        s.add(vote_base)
        s.commit()
        vote = s.refresh(vote_base)
        return vote
