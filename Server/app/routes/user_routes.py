from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.Session import get_db
from app.schemas.UserSchema import RegisterUser, LoginUser
from app.models.UserModels import User
from app.core.otp_generator import generate_otp
from app.caching.config import rd
from app.core.email_services import send_otp
from app.decorators.cache_decor import rate_limiter
from app.serializer.user_serializer import serialize_user
import json

app = APIRouter()


@app.post("/register")
async def register_user(user: RegisterUser, db: Session = Depends(get_db)):

    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists.")

    otp = generate_otp()

    temp_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        email=user.email,
        gender=user.gender,
        avatar=user.avatar,
        password=user.password,
    )

    await rd.set(name=f"temp_user:{user.email}", value=json.dumps(temp_user), ex=600)
    await rd.set(name=f"otp:{user.email}", value=otp, ex=600)

    is_sent = await send_otp(user.email, otp)

    if not is_sent:
        raise HTTPException(
            status_code=501, detail="Failed to sned OTP, Please try again later."
        )

    return {"status": 200, "message": "OTP sent successfully"}


@app.post("/verify_otp")
async def verify_otp(email: str, otp: str, db: Session = Depends(get_db)):
    if not email or not otp:
        raise HTTPException(status_code=401, detail="All fields are required")

    saved_otp = await rd.get(f"otp:{email}")
    saved_user = await rd.get(f"temp_user:{email}")

    if not saved_otp or not saved_user:
        raise HTTPException(status_code=400, detail="OTP expired or invalid")

    if saved_otp != otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    user_data = json.loads(saved_user)

    new_user = User(**user_data)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    await rd.delete(f"temp_user:{email}")
    await rd.delete(f"otp:{email}")

    return {"status": 201, "message": "Registraion successfull"}


# Helper function for Login method
def verify_password(password, db_password):
    password_hash = password
    db_hash_pass = db_password

    if password_hash == db_hash_pass:
        return True

    return False


@app.post("login")
def login_user(user: LoginUser, db: Session = Depends(get_db)):
    _user = db.query(User).filter(User.email == user.email).first()

    if not _user:
        raise HTTPException(status_code=404, detail="User not found")

    isAuthenticated = verify_password(user.password, _user.password_hash)

    if not isAuthenticated:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "status": 200,
        "message": "Success",
        "data": serialize_user(_user),
        "isAuthenticated": isAuthenticated,
    }


@app.post("/profile")
async def get_profile(email: str, db: Session = Depends(get_db)):

    saved_user = await rd.get(name=f"user:{email}")

    if saved_user:
        return {"status": 200, "message": "Success", "data": json.loads(saved_user)}

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    await rd.set(name=f"user:{email}", value=json.dumps(user), ex=1800)

    return {"status": 200, "message": "Success", "data": serialize_user(user)}
