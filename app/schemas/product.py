from decimal import Decimal

from pydantic import BaseModel, Field


class CreateProductSchema(BaseModel):
    name: str = Field(min_length=1)
    price: Decimal = Field(gt=0)
    quantity: int = Field(ge=0, strict=True)


class ProductResponseSchema(CreateProductSchema):
    id: int