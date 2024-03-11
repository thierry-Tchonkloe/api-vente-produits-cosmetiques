from fastapi import FastAPI
from models.base import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from routes.user import  user_router
from routes.product import product_router
from routes.admin import admin_router
from routes.command import command_router
# from routes.buy import buy_router
from routes.contact import contact_router
from routes.products import products_router


def create_database():
    Base.metadata.create_all(bind=engine)
    

create_database()
app = FastAPI()


# Middleware pour autoriser les requêtes CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(product_router)
app.include_router(admin_router)
app.include_router(products_router)
app.include_router(command_router)
# app.include_router(buy_router)
app.include_router(contact_router)

