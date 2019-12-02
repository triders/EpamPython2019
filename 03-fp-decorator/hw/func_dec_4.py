def applydecorator(function):
    def decorator(func):
        def inner(*args, **kwargs):
            function(*args, **kwargs)
        return inner
    return decorator


@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    return f(*args, **kwargs)

# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever


foo(40, 2)
print(*(foo(40, 2)))
'''
>>>foo
>>>40 2
'''