import os
import time
from datetime import datetime
import pickle

# API
from fastapi import FastAPI
from pydantic import BaseModel

# API request
class RequestSongs(BaseModel):
    songs: 'list[str]'

app = FastAPI()

### Processing functions ###
def getModelDatetime(path):
    mtime = os.path.getmtime(path)
    return datetime.fromtimestamp(mtime)

def getVersionFromDt(dt: datetime) -> str:
    daySeconds = dt.hour * 3600 + dt.minute * 60 + dt.second

    return f"{dt.year}.{dt.month}.{dt.day}.{daySeconds}"

# Load model on startup
modelpath = './shared/model.pickle'

# Wait for model file to be available (only needed on startup)
while not os.path.exists(modelpath):
    time.sleep(1)

model = pickle.load(open(modelpath, 'rb')) 

currentModelDatetime = getModelDatetime(modelpath)

### API Functions ###
# Used for tests
@app.get("/")
def read_root():
    return {"Message": "Github actions test"}

# Route to recommend playlists
@app.post("/api/recommender")
def insert(body: RequestSongs):
    global model
    global modelpath
    global currentModelDatetime

    # Check model modification time
    modelDatetime = getModelDatetime(modelpath)

    # Reload model if different
    if modelDatetime != currentModelDatetime:
        model = pickle.load(open(modelpath, 'rb'))
        currentModelDatetime = modelDatetime

    recommendation = []

    # Generate a playlist from user input and model
    for i in model:
        for musicaReq in body.songs:
            musicA = i[0]
            confidence = i[2]
            if (musicA.__contains__(musicaReq) and confidence > 0.5):
                recommendation.append(list(i[1])[0])         
                break

    # Generate response, model version will be updated if the model changes       
    response = {}
    response['model_version'] = getVersionFromDt(currentModelDatetime)
    response['recommended_playlist'] = sorted(list(set(recommendation)))
    
    # Fast API will automagically convert dict to json
    return response