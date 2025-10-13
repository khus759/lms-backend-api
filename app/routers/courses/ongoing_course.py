from fastapi import APIRouter
import json
import os
from app.config import ONGOING_COURSES_FILE

router = APIRouter()

if not os.path.exists(ONGOING_COURSES_FILE):
    raise FileNotFoundError(f"File not found at: {ONGOING_COURSES_FILE}")

with open(ONGOING_COURSES_FILE, "r") as f:
    ongoing_courses = json.load(f)

@router.get("/courses/ongoing")
def get_ongoing_courses():
    return ongoing_courses
