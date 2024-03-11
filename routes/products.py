# routes/products.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from functions.products import create_products, get_products
from schemas.products import ProductsCreate,  Products as ProductsResponse
from schemas.product import Product
from routes.auth import get_db
from .auth import get_current_admin

products_router = APIRouter(prefix="/products", tags=["Les actions sur les produits"], dependencies=[Depends(get_current_admin)])

@products_router.post("/", response_model=ProductsResponse)
def create_products(products: ProductsCreate, db: Session = Depends(get_db)):
    return create_products(db, products)

@products_router.get("/", response_model=list[ProductsResponse])
def read_products(skip: int = 0, limit: int = None, db: Session = Depends(get_db)):
    return get_products(db, skip=skip, limit=limit)


@products_router.get("/{products_id}", response_model=ProductsResponse)
def reads_products(products_id: int, db: Session = Depends(get_db)):
    _products = get_products(db, products_id)
    
    if _products is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Product not found"
        )
    prods = _products.products_name
    
    def out_product_id(prods: str ):
        prods2 = db.query(Product).filter(Product.product_name == prods).first()
        
        if prods2 is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Product name not found"
            )
        return prods2
    
    return out_product_id(prods)


