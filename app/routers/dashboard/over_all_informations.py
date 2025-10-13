from fastapi import APIRouter
import json
import os
from app.config import OVERVIEW_FILE

router = APIRouter()

if not os.path.exists(OVERVIEW_FILE):
    raise FileNotFoundError(f"File not found at: {OVERVIEW_FILE}")

with open(OVERVIEW_FILE, "r", encoding="utf-8") as f:
    overview_data = json.load(f)

@router.get("/dashboard/over-all-informations")
def get_overview():
    return overview_data
