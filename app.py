import config
import requests
from flask import Flask, request

app = Flask(__name__)

spoonacularBaseUrl = "https://api.spoonacular.com"
spoonacularApiKey = config.spoonacularApiKey

# api route for fetching comlex recipes https://spoonacular.com/food-api/docs#Search-Recipes-Complex
@app.route('/search-recipes', methods=['GET'])
def getRecipes():
    foodType = request.args.get('query', "") 
    cuisine = request.args.get('cuisine', "") 
    diet = request.args.get('diet', "")
    maxCalories = request.args.get('maxCalories', "")

    url = spoonacularBaseUrl + "/recipes/complexSearch"

    queryParameters = {
        "query" : foodType,
        "cuisine" : cuisine,
        "diet" : diet,
        "maxCalories" : maxCalories,
        "number" : 10,
        "apiKey" : spoonacularApiKey
    }

    results = requests.get(url=url, params=queryParameters)
    app.logger.warning(f"REQUEST URL LOG: {results.url}")

    return results.text

# api route for similar recipes https://spoonacular.com/food-api/docs#Get-Similar-Recipes
@app.route('/search-similar-recipes', methods=['GET'])
def getSimilarRecipes():
    return True

# api route for random recipes https://spoonacular.com/food-api/docs#Get-Random-Recipes
@app.route('/search-random-recipe', methods=['GET'])
def getRandomReccuipes():
    return True