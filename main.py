from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Score(BaseModel):
    name: str
    score: int

leaderboard: List[Score] = []

@app.post("/submit")
def submit_score(score: Score):
    leaderboard.append(score)
    leaderboard.sort(key=lambda s: s.score, reverse=True)
    leaderboard[:] = leaderboard[:10]
    return {"status": "ok"}

@app.get("/leaderboard")
def get_leaderboard():
    return leaderboard

