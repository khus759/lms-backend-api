from fastapi import APIRouter, HTTPException
import json
import os
from app.config import PRODUCTIVITY_FILE

router = APIRouter()

#  Check if file exists
if not os.path.exists(PRODUCTIVITY_FILE):
    raise FileNotFoundError(f"File not found at: {PRODUCTIVITY_FILE}")

#  Load JSON data
with open(PRODUCTIVITY_FILE, "r", encoding="utf-8") as f:
    productivity_data = json.load(f)

#  Endpoint
@router.get("/dashboard/productivity")
def get_productivity():
    return productivity_data
