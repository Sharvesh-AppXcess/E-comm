from sqlalchemy.orm import Session
from app.models.product import Product
from app.schema.product import ProductCreate, ProductUpdate

def create_product(
        db: Session, 
        product: ProductCreate
):
    db_product = Product(
        **product.model_dump()
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products( db: Session):
    return db.query(Product).all()

def get_product_by_id(
    db: Session,
    product_id: int
):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(
        db:Session,
        product_id: int,
        product: ProductUpdate
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        return None
    
    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.stock = product.stock
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(
        db: Session,
        product_id: int
):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        return None 
    db.delete(db_product)
    db.commit()
    return {
        "message": f"Product with id {product_id} has been deleted successfully"
    }