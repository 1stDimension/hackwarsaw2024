from fastapi import FastAPI
from localhub.admin import app as admin_mount
from localhub.voter import app as voter_mount

app = FastAPI()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


app.mount("/admin", admin_mount)
app.mount("/voter", voter_mount)
