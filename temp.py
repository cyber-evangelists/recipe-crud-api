from bson import ObjectId
import motor.motor_asyncio
import beanie
import asyncio
from bson.objectid import ObjectId
from models.re_schema import Recipe
from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()
router = APIRouter()

@router.on_event("startup")
async def startup_event():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    await beanie.init_beanie(database=client.Recipes_db, document_models=[Recipe])
    task1 = Recipe(name="Pizza", ingredients= ["test", "cheese", "green", "blue", "purple"])
    
    
app.include_router(router)


    
    
    
    

task1.insert()
    # await task1.delete()
    
    
# asyncio.run(main())

