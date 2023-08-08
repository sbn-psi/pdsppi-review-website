import os

print('load dev settings')

DEBUG = os.environ.get("DEBUG", True)

ALLOWED_HOSTS = ['*'] 

BASE_URL = 'http://localhost:8000'
print('dev DEBUG: ', DEBUG)