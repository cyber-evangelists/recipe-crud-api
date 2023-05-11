from pydantic import BaseModel, Field
from typing import Optional, List


class RecipeSchema(BaseModel):
    name: str = Field(...)              # Required
    ingredients: List[str] = Field(...) # Required

    class Config: 
        schema_extra = {
            "example": {
                "name": "Donuts",
                "ingredients": ["Flour", "Milk", "Sugar", "Vegetable Oil"]
            }
        }


class UpdateRecipeSchema(BaseModel):
    id: str
    name: Optional[str]
    ingredients: Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "id": "645b8955711af8133e5a484",
                "name": "Buns",
                "ingredients": ["Flour", "Milk", "Sugar", "Vegetable Oil"]
            }
        }
