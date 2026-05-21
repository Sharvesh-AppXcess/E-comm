from pydantic import BaseModel

class ArithmeticRequest(BaseModel):
    a: float
    b: float