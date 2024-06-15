from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from localhub.admin import app as admin_mount
from localhub.voter import app as voter_mount

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


app.mount("/admin", admin_mount)
app.mount("/voter", voter_mount)
