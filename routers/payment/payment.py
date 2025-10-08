from fastapi import APIRouter
import json
from config import PAYMENT_FILE

router = APIRouter()

@router.get("/payments")
def get_payments():
    with open(PAYMENT_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
