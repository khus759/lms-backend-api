from fastapi import APIRouter
import json
import os
from app.config import COURSE_CONTENTS_FILE

router = APIRouter()

if not os.path.exists(COURSE_CONTENTS_FILE):
    raise FileNotFoundError(f"File not found at: {COURSE_CONTENTS_FILE}")

with open(COURSE_CONTENTS_FILE, "r", encoding="utf-8") as f:
    course_contents = json.load(f)

@router.get("/explore-course/course-contents")
def get_course_contents():
    return course_contents
