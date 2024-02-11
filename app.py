from config import spoonacularApiKey, redis
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

spoonacularBaseUrl = "https://api.spoonacular.com"
spoonacularApiKey = spoonacularApiKey


# api route for fetching comlex recipes https://spoonacular.com/food-api/docs#Search-Recipes-Complex
@app.route('/search-recipes', methods=['GET'])
def getRecipes():
    foodType = request.args.get('query', None) 
    cuisine = request.args.get('cuisine', None) 
    diet = request.args.get('diet', None)
    maxCalories = request.args.get('maxCalories', None)

    # Fetch the recipe from cache, if possible
    cacheKey = f"{foodType}.{cuisine}.{diet}.{maxCalories}"
    cachedRecipe = redis.get(cacheKey)
    if (cachedRecipe is not None):
        app.logger.warn(f"Returned a cached recipe {cachedRecipe}")
        return jsonify(cachedRecipe)

    url = spoonacularBaseUrl + "/recipes/complexSearch"

    parameters = {
        "query" : foodType,
        "cuisine" : cuisine,
        "diet" : diet,
        "maxCalories" : maxCalories,
        "number" : 10,
        "apiKey" : spoonacularApiKey
    }

    # Only add the items in the query if they don't contain `None`
    queryParameters = {key : value for key, value in parameters.items() if value is not None}
    results = requests.get(url=url, params=queryParameters)

    # Cache the response
    redis.set(cacheKey, results.json())

    return jsonify(results.json())

# api route for similar recipes https://spoonacular.com/food-api/docs#Get-Similar-Recipes
@app.route('/search-similar-recipes', methods=['GET'])
def getSimilarRecipes():
    return ""

# api route for random recipes https://spoonacular.com/food-api/docs#Get-Random-Recipes
@app.route('/search-random-recipe', methods=['GET'])
def getRandomReccuipes():
    return ""