from .base import *

ALLOWED_HOSTS = ['localhost','localhost','vger.psi.edu','vger.psi.edu','borg.psi.edu']

try:
    from .local import *
except ImportError:
    pass
