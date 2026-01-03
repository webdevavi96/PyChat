from pydantic import BaseModel, EmailStr


class RegisterUser(BaseModel):
    first_name = str
    last_name = str
    phone: str
    email: EmailStr
    gender = str
    password: str
    avatar = str


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class UpdateUser(BaseModel):
    pass


class ForgotPassword(BaseModel):
    pass
