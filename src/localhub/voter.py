from fastapi import HTTPException
from fastapi import FastAPI
from localhub.models import Voter, Voters # type: ignore
from localhub.sql import Meeting,User,SessionLocal # type: ignore

app = FastAPI()

M = Meeting()
print(M)

@app.get("/")
def read_main():
    with SessionLocal() as sess:
        l = sess.query(User).all()

        s : list[Voter]= list()
        for i in l:
           s.append(
               Voter(
                   first_name=i.first_name, # type: ignore
                   last_name=i.last_name, # type: ignore
                   local=i.local, # type: ignore
                   id=i.id # type: ignore
               )
           )
    return s

@app.post("/{voter_id}/absent")
def absent(voter_id: str):
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
                   first_name=user.first_name, # type: ignore
                   last_name=user.last_name, # type: ignore
                   local=user.local, # type: ignore
                   id=user.id # type: ignore
               )
            else:
                raise HTTPException(404)
        except Exception as e:
            print(e)