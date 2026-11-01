from fastapi import FastAPI

from app.repositories.product_repository import (
    ProductRepository,
)
from app.routers.products import router as products_router


app = FastAPI(title="Order Management API")

app.state.product_repository = ProductRepository()

print("Starting Order Management API...")
print(app.state)

app.include_router(products_router)