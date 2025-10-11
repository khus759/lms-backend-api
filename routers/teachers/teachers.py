# from fastapi import APIRouter
# import json
# from config import TEACHERS_FILE

# router = APIRouter()

# @router.get("/teachers")
# def get_teachers():
#     with open(TEACHERS_FILE, "r", encoding="utf-8") as file:
#         data = json.load(file)
#     return data



from fastapi import APIRouter, HTTPException
import json
from config import TEACHERS_FILE

router = APIRouter()

@router.get("/teachers")
def get_teachers():
    with open(TEACHERS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


@router.get("/teachers/{teacher_id}")
def get_teacher_by_id(teacher_id: int):
 
    with open(TEACHERS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    for category, teachers in data.items():
        for teacher in teachers:
            if teacher.get("id") == teacher_id:
                teacher["category"] = category
                return teacher

    raise HTTPException(status_code=404, detail="Teacher not found")