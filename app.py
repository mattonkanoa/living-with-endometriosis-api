import config
import requests
from flask import Flask, request

app = Flask(__name__)
spoonacularApiKey = config.spoonacularApiKey

# api route for fetching recipes https://spoonacular.com/food-api/docs#Search-Recipes-Complex
@app.route('/search-recipes', methods=['GET'])
def getRecipes():
    # The food type e.g. rice, pasta, steak
    foodType = request.args.get('query') 
    cuisine = request.args.get('cuisine') 
    diet = request.args.get('diet')
    maxCalories = request.args.get('maxCalories')

    # Build url - TEST
    urlString = f"https://api.spoonacular.com/recipes/complexSearch?query={foodType}&number=10&apiKey={spoonacularApiKey}"
    results = requests.get(urlString)

    return results

# api route for similar recipes https://spoonacular.com/food-api/docs#Get-Similar-Recipes
@app.route('/search-similar-recipes', methods=['GET'])
def getSimilarRecipes():
    return True

# api route for random recipes https://spoonacular.com/food-api/docs#Get-Random-Recipes
@app.route('/search-random-recipe', methods=['GET'])
def getRandomRecipes():
    return True