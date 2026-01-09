from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import hashlib
import os

SECRET_KEY = os.getenv("JWT_SECRET", "CHANGE_ME")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _pre_hash(password: str) -> str:
    """
    Pre-hash password to avoid bcrypt 72-byte limit.
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def hash_password(password: str) -> str:
    return pwd_context.hash(_pre_hash(password))


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(_pre_hash(password), hashed)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
