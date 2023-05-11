from fastapi import FastAPI, Body
from config import db
from models.model import RecipeSchema, UpdateRecipeSchema
from bson import ObjectId


app = FastAPI()

@app.get("/", tags=["Home"])    # Home 
def get_root() -> dict:
    return {
        "message": "Welcome to the MyRecipe app."
    }
    
@app.get("/recipes", tags=["Recipe"])       # Get all Recipes
def get_recipes() -> dict:
    data = db.all()
    return {"data": data}

@app.get("/recipe/{id}", tags=["Recipe"])     # Get one recipe by id
def get_recipe(id: str) -> dict:                  
    if not ObjectId.is_valid(id):
        return {"error": "Invalid id"}
    
    data = db.get_one(ObjectId(id))
    return {"data": data}
       

@app.post("/recipe", tags=["Recipe"])       # Add recipe to DB
def add_recipe(recipe: RecipeSchema = Body(...)) -> dict:
    id = db.add(recipe)
    if id is None:
        return {"This recipe already exists": recipe.name}
    return {"inserted": "Recipe added successfully", "id": id, "name": recipe.name} 
    
    
@app.put("/recipe", tags=["Recipe"])        # Update the recipe
def update_recipe(recipe_data: UpdateRecipeSchema = Body(...)) -> dict:
    if not ObjectId.is_valid(recipe_data.id):
        return {"error": "Invalid id"}
    recipe_data.id = ObjectId(recipe_data.id)
    data = db.update(recipe_data)
    
    if data:
        return {"updated": "Recipe updated successfully", "updated_count": data, "name": recipe_data.name}
    return {"updated_count": data}


@app.delete("/recipe/{id}", tags=["Recipe"])        # delete a recipe
def delete_recipe(id: str) -> dict:
    if not ObjectId.is_valid(id):
        return {"error": "Invalid id"}
    
    data = db.delete(ObjectId(id))
    return {"inserted": "Recipe deleted successfully", "inserted_id": id, "deleted count": data}
    



