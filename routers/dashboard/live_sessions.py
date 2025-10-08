from fastapi import APIRouter
import json
import os
from config import LIVE_SESSIONS_FILE

router = APIRouter()

# Debug print
print("Looking for file at:", LIVE_SESSIONS_FILE)

if not os.path.exists(LIVE_SESSIONS_FILE):
    raise FileNotFoundError(f"File not found at: {LIVE_SESSIONS_FILE}")

with open(LIVE_SESSIONS_FILE, "r", encoding="utf-8") as f:
    live_sessions = json.load(f)

@router.get("/dashboard/live-sessions")
def get_live_sessions():
    return live_sessions
