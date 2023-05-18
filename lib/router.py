from fastapi import APIRouter, Depends, HTTPException
from models.recipe import Recipe
from beanie import PydanticObjectId
from bson import ObjectId
from auth.auth_bearer import JWTBearer
from email_ import get_email
from models.response import recipeResponse, All


router = APIRouter()
    
@router.get("/all", tags=["Recipe"])       # Get all Recipes
async def get_recipes() -> All:
    data = await Recipe.find_all().to_list()
    return data
        

@router.get("/{id}", tags=["Recipe"])     # Get one recipe by id
async def get_recipe(id: PydanticObjectId) -> recipeResponse:                  
        
    try:
        data = await Recipe.get(id)
        return {"name": data.name , "ingredients": data.ingredients, "message": "success"}
    except:
        raise HTTPException(status_code=404, detail="Recipe not found")
       

@router.post("/", dependencies=[Depends(JWTBearer())], tags=["Recipe"])       # Add recipe to DB
async def add_recipe(recipe: Recipe) -> recipeResponse:
    recipe.created_by = get_email()
    await Recipe.create(recipe)
    return {"name": recipe.name , "ingredients": recipe.ingredients, "message": "recipe added"}
    
    
@router.put("/{id}", dependencies=[Depends(JWTBearer())], tags=["Recipe"])        # Update the recipe
async def update_recipe(recipe_data: Recipe, id) -> recipeResponse:
    id = ObjectId(id)
    recipe_to_update = await Recipe.get(id)
    
    if recipe_to_update.created_by == get_email():
        recipe_to_update.name = recipe_data.name
        recipe_to_update.ingredients = recipe_data.ingredients
        await recipe_to_update.save()
        return {"name": recipe_to_update.name , "ingredients": recipe_to_update.ingredients, "message": "recipe updated"}
    return HTTPException(status_code=401, detail="unauthorized access")
        
    

@router.delete("/{id}", dependencies=[Depends(JWTBearer())], tags=["Recipe"])        # delete a recipe
async def delete_recipe(id) -> recipeResponse:
    id = ObjectId(id)
    recipe_to_delete = await Recipe.get(id)
    
    if recipe_to_delete.created_by == get_email():
        name = recipe_to_delete.name
        ingredients = recipe_to_delete.ingredients
        await recipe_to_delete.delete()
        return {"name": name , "ingredients": ingredients, "message": "recipe deleted"}
    return HTTPException(status_code=401, detail="unauthorized access")
        







 
    




    

