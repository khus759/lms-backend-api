from fastapi import APIRouter
import json
from config import TEACHERS_FILE

router = APIRouter()

@router.get("/teachers")
def get_teachers():
    with open(TEACHERS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
