from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.Session import get_db
from app.schemas.UserSchema import RegisterUser
from app.models.UserModels import User
from app.core.otp_generator import generate_otp
from app.caching.config import rd
from app.decorators.cache_decor import rate_limiter
import json
from Server.app.schemas.PostSchema import NewPost

app = APIRouter()


@app.post("/register")
def register_user(user: RegisterUser, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return {
            "status": 409,
            "message": "This email already existt. Please try to login or use another email address",
        }

    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        email=user.email,
        gender=user.gender,
        avatar=user.avatar,
        password=user.password,
    )

    rd.set(name="temp_user", value=json.dumps(new_user), ex=(60 * 10))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)


# These routes are just for testing perpose. These will be removed in production.
@app.get("/users/{user_id}", dependencies=[Depends(rate_limiter(3, 60))])
async def Home(user_id: int):
    cache_key = f"user_id:{user_id}"

    cache = await rd.get(cache_key)

    if cache:
        return {
            "status": 200,
            "message": "Incoming data from cache",
            "data": json.loads(cache),
        }

    data = {
        "users": [
            {
                "id": 1,
                "username": "Ravi",
                "details": [
                    {
                        "avatar": "sample.jpg",
                        "followers": 1000,
                        "following": 12,
                        "posts": {"videos": 30, "photos": 20},
                    }
                ],
            },
            {
                "id": 2,
                "username": "Satya",
                "details": [
                    {
                        "avatar": "sample.jpg",
                        "followers": 1000,
                        "following": 12,
                        "posts": {"videos": 30, "photos": 20},
                    }
                ],
            },
        ]
    }

    await rd.set(cache_key, value=json.dumps(data), ex=30)

    return {"status": 200, "message": "Incoming data forom db", "data": data}
