from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.service.order_service import place_order
from app.service.order_service import get_orders

from app.models.user import User


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/")
def create_order(
    db: Session = Depends(get_db)
):
    current_user = User(id=1)

    order = place_order(
        db,
        current_user.id
    )

    if not order:
        raise HTTPException(
            status_code=400,
            detail="Cart is empty"
        )

    return order

@router.get("/")
def view_orders(
    db: Session = Depends(get_db)
):

    current_user = User(id=1)

    return get_orders(
        db,
        current_user.id
    )