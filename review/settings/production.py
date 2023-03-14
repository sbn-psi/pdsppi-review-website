from .base import *

ALLOWED_HOSTS = ['localhost','localhost','vger.psi.edu','vger.psi.edu','sbn.psi.edu']

try:
    from .local import *
except ImportError:
    pass
