from typing import List
from beanie import Document


class Recipe(Document):  
    name: str               # Required
    ingredients: List[str]  # Required
    # created_by: str

    class Config: 
        # orm_mode = True
        schema_extra = {
            "example": {
                "name": "Donuts",
                "ingredients": ["Flour", "Milk", "Sugar", "Vegetable Oil"]
                # "created_by": "automatically-generated-username"
            }
        }