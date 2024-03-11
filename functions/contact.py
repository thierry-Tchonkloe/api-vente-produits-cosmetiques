from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib
import string
from sqlalchemy.orm import Session
from models.user import User
from fastapi import HTTPException, status
from schemas.user import UserCreate, User as UserResponse, PasswordFormat
from routes import auth


def send_contact_email(email_to: str, email_from, subject: str, message: str):
    sender_email = email_from #"0dc70c4667bbe7"  
    sender_password = "3055376bcb5bb7"  
    recipient_email = email_to
    mes = f"{message}:"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(mes, "plain"))

    try:
        server = smtplib.SMTP("sandbox.smtp.mailtrap.io", 587)  
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(recipient_email)
        server.quit()
        return True
    except:
        return False