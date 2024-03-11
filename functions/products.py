from sqlalchemy.orm import Session
from schemas.product import ProductCreate, Product as ProductResponse
from schemas.products import ProductsCreate, Products as ProductsResponse
from models.product import Product
from models.products import Products
from fastapi import HTTPException, status



def create_products(db: Session, products: ProductsCreate):
    db_products = Products(**products.dict())
    db.add(db_products)
    db.commit()
    db.refresh(db_products)
    return ProductResponse.from_orm(db_products)


def get_products(db: Session, products_id: int):
    db_products = db.query(Products).filter(Products.products_id == products_id).first()
    if db_products is None:
        return None
    return ProductResponse.from_orm(db_products)


def update_product_quantity(db: Session, product_id: int, quantity: int, movement_type: str):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()

    if db_product:
        if movement_type.lower() == "achat":
            db_product.quantity_in_stock += quantity
        elif movement_type.lower() == "vente":
            if quantity > db_product.quantity_in_stock:
                raise HTTPException(
                    status_code=status.HTTP_417_EXPECTATION_FAILED,
                    detail=' Expected failure: insuffisant quantity in stock. You can add'
                )
            else:
                db_product.quantity_in_stock -= quantity

        db.commit()
        db.refresh(db_product)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")