from pydantic import BaseModel, Field
from typing import Optional, List


class RecipeSchema(BaseModel):
    id: Optional[int]                   # Optional
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
    name: Optional[str]
    ingredients: Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "name": "Buns",
                "ingredients": ["Flour", "Milk", "Sugar", "Vegetable Oil"]
            }
        }
