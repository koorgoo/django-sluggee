from django.utils.six import *

_u = u

def u(c):
    if PY3: return c
    else:
        if isinstance(c, unicode): return c
        else: return unicode(c,'utf-8')
