from fastapi import FastAPI,APIRouter, HTTPException, Form, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from models.contact import Contact as ContactModel, Base
from schemas.contact import ContactCreate, Contact as ContactResponse
from functions.contact import send_contact_email
from routes.auth import get_db
from .auth import get_current_user

contact_router = APIRouter(prefix="/contact", tags=["Les contact pour des info"], dependencies=[Depends(get_current_user)])

app = FastAPI()

@app.post("/contact", response_model=ContactResponse)
async def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    contact_date = datetime.now()
    db_contact = ContactModel(**contact.dict, contact_date=contact_date)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)

    # # Envoyez l'e-mail avec les informations du contact
    
    email_subject = "produits cosmetique : faire commande d'un produit"
    
    email_message = f"Nom: {contact.first_name} {contact.last_name} \nTel: {contact.phone_number} \nEmail: {contact.email} \nMessage: {contact.message}"
    
    comm=send_contact_email(to_email="thierrytchonkloe79@gmail.com", email_from = contact.email, subject=email_subject, message=email_message)
    
    if comm :
        my_message = "votre contact est faite avec success"
    else :
        my_message = "contact nom faite"
    return db_contact, my_message