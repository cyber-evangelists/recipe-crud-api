from pydantic import BaseModel
from typing import List

class recipeResponse(BaseModel):
    name: str
    ingredients: List[str] 
    message: str 
    
class allRecipes(BaseModel):
    all_recipes: List[dict]
    
    
class signUp(BaseModel):
    message: str
    name: str
    
class signIn(BaseModel):
    message: str
    email: str
    token: str
    

    