from fastapi import FastAPI

app = FastAPI()


@app.get("/app")
def read_main():
    return {"message": f"Hello World from {__name__} app"}
