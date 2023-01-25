from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['localhost', 'vger.psi.edu', 'vger.psi.edu:3434'] 

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("POSTGRES_ENGINE"),
        'NAME': os.environ.get("POSTGRES_DATABASE"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        'PORT': os.environ.get("POSTGRES_PORT"),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
