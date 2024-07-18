from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine
from app.auth import authenticate_user, create_access_token

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register/", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_login(db, login=user.login)
    if db_user:
        raise HTTPException(status_code=400, detail="Login already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login/")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.login, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect login or password")
    access_token = create_access_token(data={"sub": db_user.login})
    return {"access_token": access_token, "token_type": "bearer"}

class ConnectTelegramRequest(BaseModel):
    user_id: int
    telegram_id: int

@app.post("/connect-telegram/")
def connect_telegram(request: ConnectTelegramRequest, db: Session = Depends(get_db)):
    db_user = crud.update_telegram_id(db, request.user_id, request.telegram_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
