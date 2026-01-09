from pydantic import BaseModel, EmailStr


class RegisterUser(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    gender: str
    password: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UpdateUser(BaseModel):
    pass


class ForgotPassword(BaseModel):
    pass


class VerifyOTPRequest(BaseModel):
    email: EmailStr
    otp: str


class ResendOTP(BaseModel):
    email: EmailStr