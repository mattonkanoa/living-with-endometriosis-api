import config
from flask import Flask

app = Flask(__name__)
spoonacularApiKey = config.spoonacularApiKey

# api route for fetching recipes https://spoonacular.com/food-api/docs#Search-Recipes-Complex
@app.route('/search-recipes', methods=['GET'])
def getRecipes():
    return True

# api route for similar recipes https://spoonacular.com/food-api/docs#Get-Similar-Recipes
@app.route('/search-similar-recipes', methods=['GET'])
def getSimilarRecipes():
    return True

# api route for random recipes https://spoonacular.com/food-api/docs#Get-Random-Recipes
@app.route('/search-random-recipe', methods=['GET'])
def getRandomRecipes():
    return True