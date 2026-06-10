import os

from fastapi import FastAPI

name = os.getenv("FULLNAME")

app = FastAPI()

@app.get("/")
async def hello():
    return { "message": f"Hello  {name}" }