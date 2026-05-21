from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base
from app.core.database import engine

from app.models.product import Product
from app.models.user import User
from app.router.auth import router as auth_router
from app.router.product import router as product_router

from app.models.cart import Cart
from app.router.cart import router as cart_router

from app.models.order import Order
from app.router.order import router as order_router


Base.metadata.create_all(bind=engine)


app = FastAPI(title = "E-Commerce API")
app.include_router(product_router)
app.include_router(auth_router)
app.include_router(cart_router)
app.include_router(order_router)

@app.get("/")
def root():
    return {"message": "Welcome to the E-Commerce API!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)