import os

print('load dev settings')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", True)

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://localhost:8000'
print('dev DEBUG: ', DEBUG)