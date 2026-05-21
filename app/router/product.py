from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.models.user import User
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.schema.product import ProductCreate
from app.schema.product import ProductUpdate

from app.service.product_service import create_product
from app.service.product_service import get_products
from app.service.product_service import get_product_by_id
from app.service.product_service import update_product
from app.service.product_service import delete_product

from app.core.security import get_current_user

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_user)
):

    return create_product(
        db,
        product
    )


@router.get("/")
def fetch_products(
    db: Session = Depends(get_db)
):

    return get_products(db)


@router.get("/{product_id}")
def fetch_product_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = get_product_by_id(
        db,
        product_id
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    return product


@router.put("/{product_id}")
def edit_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):

    updated_product = update_product(
        db,
        product_id,
        product
    )

    if not updated_product:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    return updated_product


@router.delete("/{product_id}")
def remove_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    deleted_product = delete_product(
        db,
        product_id
    )

    if not deleted_product:
        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    return deleted_product