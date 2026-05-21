from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from app.models.arithmetic_model import ArithmeticRequest
from app.service.arithemetic_service import ArithmeticService
from app.dependencies import get_db

router = APIRouter(
    prefix = "/arithmetic",
    tags = ["arithmetic"]
)

@router.post("/add")
def add(
    data:ArithmeticRequest,
    db: Session = Depends(get_db)
):
    result = ArithmeticService.add(data.a, data.b, db)
    return {
        "operation": "addition", 
        "result": result
        }
@router.post("/subtract")
def subtract(
    data: ArithmeticRequest,
    db: Session = Depends(get_db)
):
    result = ArithmeticService.subtract(data.a, data.b, db)
    return {
        "operation": "subtraction", 
        "result": result
        }
@router.post("/multiply")
def mulitply(
    data: ArithmeticRequest,
    db: Session = Depends(get_db)
):
    result = ArithmeticService.multiply(data.a, data.b, db)
    return {
        "operation": "multiplication", 
        "result": result
        }
@router.post("/divide") 
def divide(
    data: ArithmeticRequest,
    db: Session = Depends(get_db)
):
    try:
        result = ArithmeticService.divide(data.a, data.b, db)
        return {
            "operation": "division", 
            "result": result
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))