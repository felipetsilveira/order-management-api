from app.schemas.product import (
    CreateProductSchema,
    ProductResponseSchema,
)


class ProductRepository:
    def __init__(self):
        self.products: list[ProductResponseSchema] = []
        self.next_id = 1

    def find_by_name(
        self,
        name: str,
    ) -> ProductResponseSchema | None:
        for product in self.products:
            if product.name == name:
                return product

        return None

    def create(
        self,
        data: CreateProductSchema,
    ) -> ProductResponseSchema:
        product = ProductResponseSchema(
            id=self.next_id,
            name=data.name,
            price=data.price,
            quantity=data.quantity,
        )

        self.products.append(product)
        self.next_id += 1

        return product