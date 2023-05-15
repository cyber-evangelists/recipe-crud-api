from fastapi import APIRouter, HTTPException
from model import Recipe
from typing import List
from beanie import PydanticObjectId
from bson import ObjectId


router = APIRouter()

@router.get("/", tags=["Home"])    # Home 
async def get_root() -> dict:
    return {
        "message": "Welcome to the MyRecipe app."
    }
    
@router.get("/recipes", tags=["Recipe"])       # Get all Recipes
async def get_recipes() -> dict:
    data = await Recipe.find_all().to_list()
    return {"data": data}

@router.get("/recipe/{id}", tags=["Recipe"])     # Get one recipe by id
async def get_recipe(id: PydanticObjectId) -> dict:                  
    if not PydanticObjectId.is_valid(id):
        return {"error": "Invalid id"}
    
    data = await Recipe.get(id)
    return {"data": data}
       

@router.post("/recipe", tags=["Recipe"])       # Add recipe to DB
async def add_recipe(recipe: Recipe) -> dict:
    await Recipe.create(recipe)
    return {"inserted": "Recipe added successfully", "id": recipe.id, "name": recipe.name} 
    
    
@router.put("/recipe/{id}", tags=["Recipe"])        # Update the recipe
async def update_recipe(recipe_data: Recipe, id) -> dict:
    id = ObjectId(id)
    recipe_to_update = await Recipe.get(id)
    
    recipe_to_update.name = recipe_data.name
    recipe_to_update.ingredients = recipe_data.ingredients
    
    await recipe_to_update.save()
    return {"updated": "Recipe updated successfully"}
    


@router.delete("/recipe/{id}", tags=["Recipe"])        # delete a recipe
async def delete_recipe(id) -> dict:
    id = ObjectId(id)
    recipe_to_delete = await Recipe.get(id)
    
    await recipe_to_delete.delete()
    return {"message": "Recipe deleted successfully"}
    