from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.core.Session import get_db
from app.schemas.UserSchema import RegisterUser, LoginUser,TokenResponse
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
    if not _user:
        raise HTTPException(status_code=400, detail="Email already exists.")

    otp = generate_otp()

    temp_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        email=user.email,
        gender=user.gender,
        password=hash_password(user.password),
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
