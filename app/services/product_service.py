from app.repositories.product_repository import (
    ProductRepository,
)
from app.schemas.product import (
    CreateProductSchema,
    ProductResponseSchema,
)


class ProductAlreadyExistsError(Exception):
    pass


class ProductService:
    def __init__(
        self,
        repository: ProductRepository,
    ):
        self.repository = repository

    def create_product(
        self,
        data: CreateProductSchema,
    ) -> ProductResponseSchema:

        existing_product = (
            self.repository.find_by_name(data.name)
        )

        if existing_product is not None:
            raise ProductAlreadyExistsError(
                "Product already exists"
            )

        return self.repository.create(data)

    def get_product_by_id(
        self,
        product_id: int,
    ) -> ProductResponseSchema | None:
        return self.repository.find_by_id(product_id)