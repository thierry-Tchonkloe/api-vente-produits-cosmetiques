from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib
import string
from sqlalchemy.orm import Session
from routes.auth import get_password_hash
from models.user import User
from models.admin import Admin
from fastapi import HTTPException, status
from schemas.user import UserCreate, User as UserResponse, PasswordFormat
from schemas.admin import AdminCreate, Admin as AdminResponse
from routes.auth import verify_password, get_password_hash

def get_user(db: Session, email: str):
    db_user = db.query(User).filter(User.email == email).first()
    if db_user is None : 
        return None
    return UserResponse.from_orm(db_user)

def get_user_by_id(db: Session, id: int):
    db_user = db.query(User).filter(User.user_id == id).first()
    if db_user is None : 
        return None
    return UserResponse.from_orm(db_user)

def get_users(db: Session):
    users = db.query(User).all()
    return [UserResponse.from_orm(user) for user in users]


def create_admin(db: Session, admin_name: str, password: str, email: str):
    hashed_password = get_password_hash(password)
    db_admin = Admin(admin_name=admin_name, password=hashed_password, email=email)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return UserResponse.from_orm(db_admin)


_detail= "User not found"

def update_admin(db: Session, admin_id: int, admin: AdminCreate):
    db_admin = db.query(Admin).filter(Admin.admin_id == admin_id).first()
    if db_admin:
        for key, value in admin.dict().items():
            # if key=="password": 
            #     hashed_password = get_password_hash(value)
            #     setattr(db_user, key, hashed_password)
            # else:
            setattr(db_admin, key, value)
        db.commit()
        db.refresh(db_admin)
        return UserResponse.from_orm(db_admin)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=_detail)

# atention ?
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return UserResponse.from_orm(db_user)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=_detail)



def generate_verification_code(length=6):
    characters = string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code


def send_verification_code_email(email: str, code: str, message: str):
    sender_email = "0dc70c4667bbe7"  
    sender_password = "3055376bcb5bb7"  
    recipient_email = email
    subject = "Stock Master : Code de verification"
    mes = f"{message}: {code}"

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
    
    
    


def password_forgot(db: Session, passwords: PasswordFormat):
    admin = db.query(Admin).filter(Admin.admin_id == passwords.admin_id).first()
    if admin:
        print(f"""
                encien

                {admin.password}
            """)
        is_password_valid = verify_password(passwords.old_password, admin.password)
        print(is_password_valid)
        if is_password_valid != True:
            raise HTTPException (
            status_code=status.HTTP_406_NOT_ACCEPTABLE, 
            detail="Incorrect old password"
            )
        else:
            admin.password = get_password_hash(password=passwords.new_password)
            print(f"""
                changé

                {get_password_hash(password=passwords.new_password)}
            """)
            db.commit()
            db.refresh(admin)
            db.query(Admin).filter(Admin.admin_id == passwords.admin_id).first()
            print(f"""
                nouveau

                {admin.admin_password}
            """)
            return {
                "message" : "Password modified successfully"
            }
    else:
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )



def password_forgot_verify(db: Session, email: str, code: str):
    admin = db.query(Admin).filter(Admin.admin_email == email).first()(db, email)
    if admin:
        if admin.code == code:
            db.commit()
            db.refresh(admin)
            return admin
    return None