from fastapi import APIRouter
import json
import os
from config import COMPLETED_COURSES_FILE

router = APIRouter()

if not os.path.exists(COMPLETED_COURSES_FILE):
    raise FileNotFoundError(f"File not found at: {COMPLETED_COURSES_FILE}")

with open(COMPLETED_COURSES_FILE, "r") as f:
    completed_courses = json.load(f)

@router.get("/courses/completed")
def get_completed_courses():
    return completed_courses
