from fastapi import APIRouter
import json
from config import LIVE_HISTORY_FILE

router = APIRouter()

@router.get("/live-history")
def get_live_history():
    with open(LIVE_HISTORY_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
