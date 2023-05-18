from pydantic import BaseModel
from typing import List

class recipeResponse(BaseModel):
    name: str
    ingredients: List[str] | None = None
    message: str | None = None
    
class All(BaseModel):
    _id: str
    name: str
    ingredients: List[str]
    created_by: str
    

    