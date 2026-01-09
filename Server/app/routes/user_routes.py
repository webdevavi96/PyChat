from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.Session import get_db
from app.schemas.UserSchema import (
    RegisterUser,
    LoginUser,
    TokenResponse,
    VerifyOTPRequest,
    ResendOTP,
)
from app.core.Security import hash_password, create_access_token, verify_password

from app.models.UserModels import User
from app.core.otp_generator import generate_otp
from app.caching.config import rd
from app.core.email_services import send_otp
from app.decorators.cache_decor import rate_limiter
from app.serializer.user_serializer import serialize_user
import json


app = APIRouter(prefix="/auth", tags=["Auth"])


@app.post("/register")
async def register_user(user: RegisterUser, db: Session = Depends(get_db)):
    _user = db.query(User).filter(User.email == user.email).first()
    if _user:
        raise HTTPException(status_code=400, detail="Email already exists.")

    otp = generate_otp()
    user_email = user.email.strip().lower()
    temp_user_data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone": user.phone,
        "email": user_email,
        "gender": user.gender,
        "password_hash": hash_password(user.password),
    }

    await rd.set(
        name=f"temp_user:{user_email}", value=json.dumps(temp_user_data), ex=600
    )

    await rd.set(name=f"otp:{user_email}", value=otp, ex=600)

    is_sent = await send_otp(user_email, otp)

    if not is_sent:
        raise HTTPException(
            status_code=501, detail="Failed to sned OTP, Please try again later."
        )

    return {"status": 200, "message": "OTP sent successfully"}


# Helper function for otp verification
def normalize_redis_value(value):
    if value is None:
        return None
    if isinstance(value, bytes):
        return value.decode()
    return value


@app.post("/verify_otp")
async def verify_otp(payload: VerifyOTPRequest, db: Session = Depends(get_db)):
    saved_otp = await rd.get(f"otp:{payload.email}")
    saved_user = await rd.get(f"temp_user:{payload.email}")

    if not saved_otp or not saved_user:
        raise HTTPException(status_code=400, detail="OTP expired or invalid")

    saved_otp = normalize_redis_value(saved_otp)
    saved_user = normalize_redis_value(saved_user)

    if not saved_otp or not saved_user:
        raise HTTPException(status_code=400, detail="OTP expired or invalid")

    if saved_otp != payload.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    user_data = json.loads(saved_user)
    new_user = User(**user_data)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    await rd.delete(f"temp_user:{payload.email}")
    await rd.delete(f"otp:{payload.email}")

    return {"status": 201, "message": "Registration successful"}


@app.post("/resend_otp")
async def resend(payload: ResendOTP, db: Session = Depends(get_db)):
    saved_user = await rd.get(f"temp_user:{payload.email}")

    if not saved_user:
        raise HTTPException(status_code=404, detail="Please register first")
    otp = generate_otp()
    if not otp:
        raise HTTPException(status_code=501, detail="Internal servr error")

    _is_sent = send_otp(payload.email, otp)

    if not _is_sent:
        raise HTTPException(status_code=501, detail="Internal server error")

    await rd.set(name=f"otp:{payload.email}", value=otp, ex=600)
    
    return {"stauts": 200, "message": "OTP sent successfully"}


@app.post("/login", response_model=TokenResponse)
def login_user(payload: LoginUser, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": token,
        "token_type": "bearer",
    }


@app.post("/profile")
async def get_profile(user_id: int, db: Session = Depends(get_db)):

    user_key = f"user:{user_id}"
    saved_user = await rd.get(name=user_key)

    if saved_user:
        return {"status": 200, "message": "Success", "data": json.loads(saved_user)}

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    await rd.set(name=user_key, value=json.dumps(user), ex=1800)

    return {"status": 200, "message": "Success", "data": serialize_user(user)}
