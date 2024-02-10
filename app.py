import config
import requests
from flask import Flask, request

app = Flask(__name__)

spoonacularBaseUrl = "https://api.spoonacular.com"
spoonacularApiKey = config.spoonacularApiKey

# api route for fetching comlex recipes https://spoonacular.com/food-api/docs#Search-Recipes-Complex
@app.route('/search-recipes', methods=['GET'])
def getRecipes():
    foodType = request.args.get('query', None) 
    cuisine = request.args.get('cuisine', None) 
    diet = request.args.get('diet', None)
    maxCalories = request.args.get('maxCalories', None)

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