from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

DATA_FILE = "scores.json"

class Score(BaseModel):
    name: str
    score: int

@app.get("/leaderboard")
def get_leaderboard() -> List[Score]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data

@app.post("/submit")
def submit_score(score: Score):
    scores = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            scores = json.load(f)

    scores.append(score.model_dump())  # ← use this instead of .dict()

    with open(DATA_FILE, "w") as f:
        json.dump(scores, f)

    return {"message": "Score submitted"}
