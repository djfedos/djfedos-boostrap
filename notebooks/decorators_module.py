# this module should demonstrate the import of decorators, but
# there are problems with import to jupyter notebooks,
# so I've made a special separate file that imports from here

import functools


def do_twice(func):
    @functools.wraps(func)  # to save func() __name__ and __doc__ intact by wrapper
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper
