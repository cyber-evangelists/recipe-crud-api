from fastapi import FastAPI
from router import router
from db import startup_db

app = FastAPI()

@app.on_event("startup")
async def connect():
    await startup_db()

app.include_router(router, prefix="/api")

