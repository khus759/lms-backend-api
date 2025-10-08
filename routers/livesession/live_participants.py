# live_participants.py
from fastapi import APIRouter
import json
from config import LIVE_PARTICIPANTS_FILE  

router = APIRouter()

@router.get("/live-participants")
def get_live_participants():
    
    with open(LIVE_PARTICIPANTS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
