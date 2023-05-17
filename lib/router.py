from fastapi import APIRouter, Depends
from models.recipe import Recipe
from models.user import User
from typing import List
from beanie import PydanticObjectId
from bson import ObjectId
from auth.auth_bearer import JWTBearer


router = APIRouter()
    
@router.get("/all", tags=["Recipe"])       # Get all Recipes
async def get_recipes() -> dict:
    data = await Recipe.find_all().to_list()
    return {"data": data}

@router.get("/{id}", tags=["Recipe"])     # Get one recipe by id
async def get_recipe(id: PydanticObjectId) -> dict:                  
    if not PydanticObjectId.is_valid(id):
        return {"error": "Invalid id"}
    
    data = await Recipe.get(id)
    return {"data": data}
       

@router.post("/", dependencies=[Depends(JWTBearer())], tags=["Recipe"])       # Add recipe to DB
async def add_recipe(recipe: Recipe) -> dict:
    await Recipe.create(recipe)
    return {"inserted": "Recipe added successfully", "id": recipe.id, "name": recipe.name} 
    
    
@router.put("/{id}", dependencies=[Depends(JWTBearer())], tags=["Recipe"])        # Update the recipe
async def update_recipe(recipe_data: Recipe, id) -> dict:
    id = ObjectId(id)
    recipe_to_update = await Recipe.get(id)
    
    recipe_to_update.name = recipe_data.name
    recipe_to_update.ingredients = recipe_data.ingredients
    
    await recipe_to_update.save()
    return {"updated": "Recipe updated successfully"}
    


@router.delete("/{id}", dependencies=[Depends(JWTBearer())], tags=["Recipe"])        # delete a recipe
async def delete_recipe(id) -> dict:
    id = ObjectId(id)
    recipe_to_delete = await Recipe.get(id)
    
    await recipe_to_delete.delete()
    return {"message": "Recipe deleted successfully"}






    

