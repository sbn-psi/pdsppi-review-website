from .base import *

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
