from fastapi import FastAPI,APIRouter, HTTPException, Form, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from models.command import Command as CommandModel, Base
from schemas.command import CommandCreate, Command as CommandResponse
from functions.command import send_command_email
from routes.auth import get_db
from .auth import get_current_user

command_router = APIRouter(prefix="/command", tags=["Les commande des produits"])#, dependencies=[Depends(get_current_user)])

app = FastAPI()

@app.post("/command", response_model=CommandResponse)
async def create_command(command: CommandCreate, db: Session = Depends(get_db)):
    command_date = datetime.now()
    db_command = CommandModel(**command.dict, command_date=command_date)
    db.add(db_command)
    db.commit()
    db.refresh(db_command)

    # # Envoyez l'e-mail avec les informations du contact
    
    email_subject = "produits cosmetique : faire commande d'un produit"
    
    email_message = f"Email: {command.email} \nMessage: {command.detail}"
    
    comm=send_command_email(to_email="thierrytchonkloe79@gmail.com", email_from = command.email, subject=email_subject, message=email_message)
    
    my_message=None
    
    if comm :
        my_message = "votre commande est faite avec success"
    else :
        my_message = "message nom envoyer"
        
    return db_command, my_message