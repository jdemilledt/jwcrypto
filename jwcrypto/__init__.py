import sys
import importlib


class _JWCRoot:
    def __getattr__(self, name):
        if name == '__path__':
            return __path__
        mod = importlib.import_module(".{}".format(name), __name__)
        return mod


sys.modules[__name__] = _JWCRoot()
