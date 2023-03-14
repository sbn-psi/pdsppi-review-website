from .base import *

ALLOWED_HOSTS = ['localhost','vger.psi.edu','vger.psi.edu:3434','sbn.psi.edu']

try:
    from .local import *
except ImportError:
    pass
