from sqlalchemy.orm import Session
from app.models.arithmetic_db_model import Arithmetic

class ArithmeticService:
    
    @staticmethod
    def add(a:float,b:float, db: Session):
        result = a+b
        data = Arithmetic(
            operation="addition", 
            a=a, 
            b=b, 
            result=result
        )
        db.add(data)
        db.commit()
        return result
    
    @staticmethod
    def subtract(a:float,b:float, db:Session):
        result =  a-b
        data = Arithmetic(
            operation="Subtraction",
            a=a,
            b=b,
            result=result
        )
        db.add(data)
        db.commit()
        return result
    
    @staticmethod
    def multiply(a:float,b:float, db:Session):
        result = a*b
        data = Arithmetic(
            operation="Multiplication",
            a=a,
            b=b,
            result=result
        )
        db.add(data)
        db.commit()
        return result

    @staticmethod
    def divide(a:float,b:float, db:Session):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = a/b
        data = Arithmetic(
            operation="Division",
            a=a,
            b=b,
            result=result
        )
        db.add(data)
        db.commit()
        return result