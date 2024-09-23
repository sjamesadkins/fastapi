from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome():
    return {"Welcome: This is the best site"}


@app.get("/hello")
def hello():
    return {"Hello": "How are you?"}
