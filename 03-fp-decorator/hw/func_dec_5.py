import time
import datetime
import functools
import math

FUNCTION_METRICS = {}

CACHE = {}


def count_calls_and_time(func, metrics):

    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            res = func(*args, **kwargs)
            stop = time.time()
            run_time = round(stop - start, 4)
        except:
            res = 'unavailable'
            run_time = math.inf
        metric = {args[0].__name__: run_time}
        if args[1] not in metrics:
            metrics.update({args[1]: metric})
        else:
            metrics[args[1]].update(metric)
        return res
    return wrapper


def fib_num(func, n):
    """returns n'th fibonacci number using given function"""
    return func(n), n


# 1 recursive

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
    fib = [0, 1]
    for i in range(n-1):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]


# formula
# big errors
def fib_formula(n):
    sq5 = math.sqrt(5)
    return int(((0.5 + sq5/2)**n - (0.5 - sq5/2)**n)/sq5)


def choose_best_fib(metrics):
    max_fib = metrics[max(metrics)]
    min_time = {'some_func': math.inf}
    for key, value in max_fib.items():
        if value < list(min_time.values())[0]:
            min_time = {key: value}
    res = f'Best fuction is {list(min_time.keys())[0]}'
    return res


# apply decorator

fib_num = count_calls_and_time(fib_num, FUNCTION_METRICS)

fib_num(fib_recursive, 30)
fib_num(fib_recursive, 1000)
fib_num(fib_recursive, 10000)

fib_num(fib_recursive_cache, 30)
fib_num(fib_recursive_cache, 1000)
fib_num(fib_recursive_cache, 10000)

fib_num(fib_dynamic, 30)
fib_num(fib_dynamic, 1000)
fib_num(fib_dynamic, 10000)

# print results

print(choose_best_fib(FUNCTION_METRICS))

for i in FUNCTION_METRICS.items():
    print(f'\n{i[0]}th Fib number:')
    for j in i[1].items():
        print(f'Function - {j[0]}, time = {j[1]}')


