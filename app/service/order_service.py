from sqlalchemy.orm import Session
from app.models.order import Order
from app.models.cart import Cart

def place_order(
        db: Session,
        user_id: int
):
    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()
    if not cart_items:
        return None
    total = 0
    for item in cart_items:
        total += item.quantity * item.product.price
    
    order = Order(
        user_id=user_id,
        total_price=total
    )
    db.add(order)
    db.commit() 
    db.refresh(order)

    for item in cart_items:
        db.delete(item)
    db.commit()
    return order

def get_orders(
        db: Session,
        user_id: int
):
    return db.query(Order).filter(Order.user_id == user_id).all()
