"""
Напишите реализацию функции make_it_count, которая принимает в качестве
аргументов некую функцию (обозначим ее func) и имя глобальной переменной
(обозначим её counter_name), возвращая новую функцию, которая ведет себя
в точности как функция func, за тем исключением, что всякий раз при вызове
инкрементирует значение глобальной переменной с именем counter_name.
"""

counter_name = 10


def func(counter):
    counter /= 2
    return counter


def make_it_count(function, counter):

    def new_function(function, counter):

        counter += 1
        return function(counter)

    return new_function(function, counter)


a = make_it_count
print(a(func, counter_name))


