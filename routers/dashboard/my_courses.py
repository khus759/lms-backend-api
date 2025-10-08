from fastapi import APIRouter
import json
import os
from config import MY_COURSES_FILE

router = APIRouter()

if not os.path.exists(MY_COURSES_FILE):
    raise FileNotFoundError(f"File not found at: {MY_COURSES_FILE}")

with open(MY_COURSES_FILE, "r", encoding="utf-8") as f:
    my_courses = json.load(f)

@router.get("/dashboard/my-courses")
def get_my_courses():
    return my_courses
