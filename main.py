from fastapi import FastAPI, Body
from models.model import RecipeSchema, UpdateRecipeSchema
from fastapi.encoders import jsonable_encoder
    

app = FastAPI()

recipes = [
    {
        "id": 1,
        "name": "Spaghetti Carbonara",
        "ingredients": ["Spaghetti", "Eggs", "Pancetta", "Parmesan Cheese"]
    },
    {
        "id": 2,
        "name": "Chicken Alfredo",
        "ingredients": ["Chicken Breasts", "Heavy Cream", "Garlic", "Pasta"]
    },
    {
        "id": 3,
        "name": "Beef Stroganoff",
        "ingredients": ["Beef Sirloin", "Sour Cream", "Onion", "Mushrooms"]
    },
    
    {
        "id": 4,
        "name": "Donuts",
        "ingredients": ["Flour", "Milk", "Sugar", "Vegetable Oil"]
    },
    
    {
        "id": 5,
        "name": "Beef Tacos",
        "ingredients": ["Ground beef", "Taco seasoning", "Taco shells", "Lettuce", "Tomatoes", "Cheese", "Sour cream"]
    },
]

@app.get("/", tags=["Home"])
def get_root() -> dict:
    return {
        "message": "Welcome to the MyRecipe app."
    }
    
@app.get("/recipes", tags=["Recipe"])
def get_recipes() -> dict:
    return {
        "data": recipes
    }

@app.get("/recipe/{id}", tags=["Recipe"])
def get_recipe(id: int) -> dict:
    if id > len(recipes) or id < 1:
        return {
            "error": "Invalid ID passed."
        }

    for recipe in recipes:
        if recipe['id'] == id:
            return {
                "data": [
                    recipe
                ]
            }

    return {
        "error": "No such recipe with ID {} exist".format(id)
    }
    
@app.post("/recipe", tags=["Recipe"])
def add_recipe(recipe: RecipeSchema = Body(...)) -> dict:
    recipe.id = len(recipes) + 1
    recipes.append(recipe.dict())
    return {
        "message": "Recipe added successfully."
    }
    
@app.put("/recipe", tags=["Recipe"])
def update_recipe(id: int, recipe_data: UpdateRecipeSchema) -> dict:
    stored_recipe = {}
    for recipe in recipes:
        if recipe["id"] == id:
            stored_recipe = recipe
        
    if not stored_recipe:
        return {
                "error": "No such recipe exists."
            }
    
    stored_recipe_model = RecipeSchema(**stored_recipe)
    update_recipe = recipe_data.dict(exclude_unset=True)
    updated_recipe = stored_recipe_model.copy(update=update_recipe)
    recipes[recipes.index(stored_recipe_model)] = jsonable_encoder(updated_recipe)

    return {
        "message": "Recipe updated successfully."
    }

@app.delete("/recipe/{id}", tags=["Recipe"])
def delete_recipe(id: int) -> dict:
    if id > len(recipes) or id < 1:
        return {
            "error": "Invalid ID passed"
        }

    for recipe in recipes:
        if recipe['id'] == id:
            recipes.remove(recipe)
            return {
                "message": "Recipe deleted successfully."
            }

    return {
        "error": "No such recipe with ID {} exist".format(id)
    }
    



