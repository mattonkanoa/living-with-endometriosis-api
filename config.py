import os
import redis

# Secrets
spoonacularApiKey = os.environ.get('SPOONACULAR_API_KEY')

# Redis
redis = redis.from_url(os.environ.get('REDIS_URL'))