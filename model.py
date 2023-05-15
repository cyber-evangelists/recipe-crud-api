from typing import List
from beanie import Document


class Recipe(Document):  
    name: str             # Required
    ingredients: List[str]  # Required

    class Config: 
        # orm_mode = True
        schema_extra = {
            "example": {
                "name": "Donuts",
                "ingredients": ["Flour", "Milk", "Sugar", "Vegetable Oil"]
            }
        }