from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str
    price : float
    stock : int

class ProductUpdate(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class ProductResponse(ProductCreate):
    id: int

    class config:
        from_attributes = True
