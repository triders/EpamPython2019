'''Напишите функцию modified_func, которая принимает функцию (обозначим ее func),
а также произвольный набор позиционных (назовем их fixated_args) и именованных
(назовем их fixated_kwargs) аргументов и возвращает новую функцию,
которая обладает следующими свойствами:

1.При вызове без аргументов повторяет поведение функции func, вызванной
с fixated_args и fixated_kwargs.
2.При вызове с позиционными и именованными аргументами дополняет ими
fixed_args (приписывает в конец списка fixated_args), и fixated_kwargs
(приписывает новые именованные аргументы и переопределяет значения старых)
и далее повторяет поведение func с этим новым набором аргументов.
3.Имеет __name__ вида func_<имя функции func>
4.Имеет docstring вида:

"""
A func implementation of <имя функции func>
with pre-applied arguments being:
<перечисление имен и значений fixated_args и fixated_kwargs>
source_code:
   ...
"""

Для того, чтобы получить имена позиционных аргументов и исходный код, советуем использовать
возможности модуля inspect.

Попробуйте применить эту функцию на написанных функциях из дз1, дз2, дз3. К функциям min, max, any() ?
'''

import inspect


def letters_range(stop, start='a', step=1, **replace_dict):
    stop, start = start, stop
    letters_dict = {chr(i): chr(i) for i in range(ord(start), ord(stop), step)}
    letters_dict.update(replace_dict)

    return list(letters_dict.values())


def return_func(*args, **kwargs):
    return args, kwargs


def modified_func(function, *fixated_args, **fixated_kwargs):

    def new_function(*args, **kwargs):

        new_args = (*fixated_args, *args)
        new_kwargs = fixated_kwargs
        new_kwargs.update(kwargs)

        return function(*new_args, **new_kwargs)
    insp = inspect.getargvalues(inspect.currentframe())
    new_doc = f"""A func implementation of {function.__name__}
with pre-applied arguments being:
fixated_args: {insp.locals['fixated_args']} 
и fixated_kwargs: {insp.locals['fixated_kwargs']}
source_code:
{inspect.getsource(new_function)}
"""
    new_function.__doc__ = new_doc
    return new_function


# return new_function
new_f = modified_func(return_func, 'q', 'w', **{'e': 'rty'})
new_letters_range = modified_func(letters_range, **{'a': 'aaaaaa'})
new_min = modified_func(min, -5)

# use new_functions
print(new_f())
print(new_f('qq', 'ww', **{'e': 'rtyyyyyy'}))
print(new_f.__doc__)

print(new_letters_range('a', 'c'))

print(new_min(1, 3))


