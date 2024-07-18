from pydantic import BaseModel

class UserBase(BaseModel):
    login: str
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True  # обновлено для Pydantic V2

class UserLogin(BaseModel):
    login: str
    password: str
