from fastapi import FastAPI
from pydantic import BaseModel
from logic.difficulty import get_next_difficulty
from typing import Optional
import json
from datetime import datetime

LOG_FILE = "difficulty_log.json"

app = FastAPI()

class ScoreInput(BaseModel):
    scores: list[int]
    prev_difficulty: Optional[str] = "medium"

@app.post("/next-difficulty")
def next_difficulty(data: ScoreInput):
    new_diff = get_next_difficulty(data.scores, data.prev_difficulty)

    result = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "scores": data.scores,
        "previous_difficulty": data.prev_difficulty,
        "next_difficulty": new_diff
    }

    # Append to log file
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(result) + "\n")
    except Exception as e:
        print(f"Error writing log: {e}")

    return result

@app.get("/")
def home():
    return {
        "message": "Welcome to Difficulty Adjustment API",
        "usage": "POST /next-difficulty with JSON { 'scores': [..], 'prev_difficulty': 'easy|medium|hard' }"
    }
