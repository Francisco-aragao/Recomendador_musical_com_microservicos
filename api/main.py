from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

class RequestSongs(BaseModel):
    songs: list[str]

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

#@app.post(.../api/recommend) #route to recommend playlists
@app.post("/insert/")
def insert(body: RequestSongs):
    return body
