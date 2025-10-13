from fastapi import APIRouter, HTTPException
import json, os
from app.config import QUES_ANS_FILE

router = APIRouter()

@router.get("/quiz/questions")
def get_questions():
    if not os.path.exists(QUES_ANS_FILE):
        raise HTTPException(status_code=404, detail="File not found")
    with open(QUES_ANS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
