from sqlalchemy.orm import Session
from app.models.cart import Cart
from app.models.product import Product

def add_to_cart(
    db: Session,
    user_id: int,
    product_id: int,
    quantity: int
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product: 
        return None
    
    cart_item = Cart(
        user_id=user_id, 
        product_id=product_id, 
        quantity=quantity
    )
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

def get_cart(
        db: Session,
        user_id: int
):
    return db.query(Cart).filter(Cart.user_id == user_id).all()

def remove_from_cart(
        db: Session,
        cart_id: int,
        user_id: int
):
    cart_item = db.query(Cart).filter(
        Cart.id == cart_id,
        Cart.user_id == user_id
    ).first()

    if not cart_item:
        return None
    
    db.delete(cart_item)
    db.commit()
    db.refresh(cart_item)
    return {
        "message": f"Cart item with id {cart_id} has been removed successfully"
    }