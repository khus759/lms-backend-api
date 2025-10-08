from fastapi import APIRouter
import json
from config import LIVE_ONGOING_FILE

router = APIRouter()

@router.get("/live-ongoing")
def get_ongoing():
    with open(LIVE_ONGOING_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
