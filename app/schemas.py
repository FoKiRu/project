from pydantic import BaseModel

class UserBase(BaseModel):
    login: str
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    telegram_id: int = None  # Telegram id

    class Config:
        from_attributes = True  # Pydantic V2

class UserLogin(BaseModel):
    login: str
    password: str
