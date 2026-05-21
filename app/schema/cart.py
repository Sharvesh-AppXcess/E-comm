from pydantic import BaseModel

class CartCreate(BaseModel):
    quantity: int
    