from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from app.dependencies import get_product_service
from app.schemas.product import (
    CreateProductSchema,
    ProductResponseSchema,
)
from app.services.product_service import (
    ProductAlreadyExistsError,
    ProductService,
)


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.post(
    "",
    response_model=ProductResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_product(
    data: CreateProductSchema,
    service: Annotated[
        ProductService,
        Depends(get_product_service),
    ],
):
    try:
        return service.create_product(data)

    except ProductAlreadyExistsError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error
    

@router.get(
    "",
    response_model=str,
)
def list_products(
    service: Annotated[
        ProductService,
        Depends(get_product_service),
    ],
):
    return "Deu certo"