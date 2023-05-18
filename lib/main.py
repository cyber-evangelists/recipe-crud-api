from fastapi import FastAPI
from models.user import User
from db import startup_db
from router import router
from encrypt import encrypt
from auth.auth_handler import signJWT
from email_ import set_email

app = FastAPI()

@app.on_event("startup")
async def connect():
    await startup_db()

    
@app.get("/", tags=["Home"])    # Home 
async def get_root() -> dict:
    return {
        "message": "Welcome to the MyRecipe app."
    }
    
@app.post("/user/signup", tags=["user"])       # signup
async def signup(user: User) -> dict:
    user.password = encrypt(user.password)
    await User.create(user)
    return {"inserted": "user added", "name": user.name} 


@app.get("/user/login", tags=["user"])       # login
async def login(email: str, password: str) -> dict:
    password = encrypt(password)
    db_user= await User.find_one({"email": email, "password": password})
    if db_user:
        token = signJWT(email)
        set_email(email)
        return{"user": "logged in", "email": email, "token": token}
    return {"error": "invalid credentials"}

    
app.include_router(router, prefix="/recipe")

