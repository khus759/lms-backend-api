from fastapi import APIRouter
import json
from app.config import MESSAGE_FILE

router = APIRouter()

@router.get("/messages")
def get_messages():
    with open(MESSAGE_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
