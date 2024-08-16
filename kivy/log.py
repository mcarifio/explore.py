import icecream as ic
import logging

def logger(name, level=logging.DEBUG):
    result = logging.getLogger(name)
    result.setLevel(level)
    _debug_method = result.debug
    result.debug = lambda *args, **kwargs: _debug_method(ic.argumentToString(' '.join(map(str, args))), **kwargs)
    return result

