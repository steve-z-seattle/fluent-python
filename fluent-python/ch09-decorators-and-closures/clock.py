import time

"""
`clock' is a decorator that clocks every invocation of the decorated fucntion
and displays the elapsed time, the arguments passed, and the result of the call.
"""

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked
