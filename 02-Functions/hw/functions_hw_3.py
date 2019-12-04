"""
Напишите реализацию функции make_it_count, которая принимает в качестве
аргументов некую функцию (обозначим ее func) и имя глобальной переменной
(обозначим её counter_name), возвращая новую функцию, которая ведет себя
в точности как функция func, за тем исключением, что всякий раз при вызове
инкрементирует значение глобальной переменной с именем counter_name.
"""


counter_name_1 = 10
counter_name_2 = 20


def func(*args):

    new_args = []
    for arg in args:
        new_args.append(arg/2)

    return new_args


def make_it_count(function, *counter_names):

    def new_function(*args):
        for name in counter_names:
            globals()[name] += 1
        return function(*args)

    return new_function


a = make_it_count(func, 'counter_name_1', 'counter_name_2')
print(counter_name_1, counter_name_2)
lst = a(*[1, 2, 3])
print(counter_name_1, counter_name_2)
