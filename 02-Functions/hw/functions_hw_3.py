"""
Напишите реализацию функции make_it_count, которая принимает в качестве
аргументов некую функцию (обозначим ее func) и имя глобальной переменной
(обозначим её counter_name), возвращая новую функцию, которая ведет себя
в точности как функция func, за тем исключением, что всякий раз при вызове
инкрементирует значение глобальной переменной с именем counter_name.
"""

counter_name = 10


def func(*args):

    new_args = []
    for arg in args:
        new_args.append(arg/2)

    return new_args


def make_it_count(function, counter_name):

    def new_function(*args):

        globals()[counter_name] += 1
        return function(*args)

    return new_function


a = make_it_count(func, 'counter_name')
print(counter_name)
lst = a(*[1, 2, 3])
print(counter_name)
