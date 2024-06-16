from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from localhub.admin import app as admin_mount
from localhub.voter import app as voter_mount

from localhub.sql import SessionLocal
import localhub.sql
from localhub.models import CreateBill, Bill
import sqlalchemy

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


@app.post("/bill")
def new_bill(bill: CreateBill):
    with SessionLocal() as s:
        new_bill = localhub.sql.BillBase(
            contents=bill.contents,
            creation_date=datetime.now().timestamp(),
        )
        s.add(new_bill)
        s.commit()
        s.refresh(new_bill)
        b = Bill(
            id=new_bill.id,
            contents=new_bill.contents
        )
        return b


@app.get("/bill")
def all_bills():
    with SessionLocal() as sess:
        bills = sess.query(localhub.sql.BillBase).all()
        return bills


@app.get("/bill/{bill_id}")
def old_bill(bill_id: str):
    with SessionLocal() as sess:
        print(bill_id)
        try:
            fetched_bill = sess.query(localhub.sql.BillBase).filter(
                localhub.sql.BillBase.id == bill_id).one_or_none()
            # all = sess.query(User).all()
            # for i in all:
            # s = "".join(voter_id.split("-"))
            # if s is voter_id:
            # print(f"Mam cię {i.first_name}, {i.id}")
            # print(f"{i.first_name}, {i.id}, comp {s}: {voter_id}")
            # print(user)
            if fetched_bill:
                return Bill(
                    id=fetched_bill.id,
                    content=fetched_bill.contents,
                )
            else:
                raise HTTPException(404)
        except sqlalchemy.exc.SQLAlchemyError as e:
            print(e)


app.mount("/admin", admin_mount)
app.mount("/voter", voter_mount)
