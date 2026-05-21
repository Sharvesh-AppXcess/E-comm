from sqlalchemy import Column,Integer, Float, String
from app.database import Base

class Arithmetic(Base):
    __tablename__ = "arithmetic_operations"
    id = Column(Integer,primary_key=True,index=True)
    operation = Column(String)
    a = Column(Float)
    b = Column(Float)
    result = Column(Float)
