from fastapi import APIRouter
import json
import os
from app.config import TOP_COURSES_FILE

router = APIRouter()

if not os.path.exists(TOP_COURSES_FILE):
    raise FileNotFoundError(f"File not found at: {TOP_COURSES_FILE}")

with open(TOP_COURSES_FILE, "r", encoding="utf-8") as f:
    top_courses_data = json.load(f)

@router.get("/dashboard/top-courses")
def get_top_courses():
    return top_courses_data
