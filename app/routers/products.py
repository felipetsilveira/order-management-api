from fastapi import APIRouter, status

from app.schemas.product import ProductResponse

router = APIRouter()


@router.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product(product: ProductResponse) -> ProductResponse:
    return product