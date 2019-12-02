import time
import datetime
import functools
import math

FUNCTION_METRICS = {}
CACHE = {}


def count_calls_and_time(func, metrics):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        run_time = stop - start
        if func.__name__ not in metrics:
            metric = {func.__name__: {0: round(run_time, 4)}}
            metrics.update(metric)
        else:
            metric = {len(metrics[func.__name__]): round(run_time, 4)}
            metrics[func.__name__].update(metric)
        return res
    return wrapper


def fib_num(func, n):
    """returns n'th fibonacci number using given function"""
    @functools.wraps(func)
    def wrapper(num):
        return func(num)
    return wrapper(n)


# 1 recursive

# can not count time with recursive calls


def fib_recursive(n):
    if n in (1, 2):
        return 1
    return fib_recursive(n-1)+fib_recursive(n-2)


# 2 recursive with cache


def fib_recursive_cache(n):
    if n in CACHE:
        return CACHE[n]
    elif n in (1, 2):
        return 1
    else:
        res = fib_recursive_cache(n-2) + fib_recursive_cache(n-1)
        CACHE[n] = res
        return res

# 3 dynamic


def fib_dynamic(n):
    fib = [0, 1, 1]
    for i in range(n-2):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


# apply decorator

fib_num = count_calls_and_time(fib_num, FUNCTION_METRICS)

print(fib_num(fib_recursive, 30))
print(fib_num(fib_recursive_cache, 1000))
print(fib_num(fib_dynamic, 1000))

print(FUNCTION_METRICS)