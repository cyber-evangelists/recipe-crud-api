import beanie
from models.recipe import Recipe
from models.user import User
import motor.motor_asyncio



async def startup_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    await beanie.init_beanie(database=client["Recipes_db"], document_models=[Recipe, User])
      
    
    
 