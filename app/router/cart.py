from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schema.cart import CartCreate
from app.service.cart_service import add_to_cart, get_cart, remove_from_cart
from app.core.security import get_current_user
from app.models.user import User    

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

@router.post("/{product_id}")
def add_product_to_cart(
    product_id: int,
    cart: CartCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    cart_item = add_to_cart(
        db,
        current_user.id,
        product_id,
        cart.quantity
    )

    if not cart_item:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return cart_item

@router.get("/")
def view_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_cart(
        db,
        current_user.id
    )

@router.delete("/{cart_id}")
def remove_product_from_cart(
    cart_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = remove_from_cart(
        db,
        cart_id,
        current_user.id
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )

    return result