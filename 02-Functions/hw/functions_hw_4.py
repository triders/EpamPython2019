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
import collections


def print_func(*args, **kwargs):
    return args, kwargs


def modified_func(function, *fixated_args, **fixated_kwargs):

    def new_function(*args1, **kwargs1):

        p_values = list(inspect.signature(function).parameters.values())
        func_args = p_values[0]
        print(func_args)
        func_kwargs = p_values[1]
        print(func_kwargs)
        '''
        d = dict(func_kwargs)
        d.update(fixated_kwargs)
        d.update(**kwargs1)
        '''
        d = dict(fixated_kwargs)
        d.update(kwargs1)
        return function(*func_args, *fixated_args, *args1, **d)

    return new_function


# return new_function
new_f = modified_func(print_func, 'q', 'w', **{'c': 'er', 'd': 'ty'})

# use new_function
print(new_f())
print(new_f('aa', 'bb', **{'c': 'err', 'd': 'tyy'}))



