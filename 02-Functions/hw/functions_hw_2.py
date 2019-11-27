"""
Напишите реализацию функции atom, которая инкапсулирует некую переменную,
предоставляя интерфейс для получения и изменения ее значения,
таким образом, что это значение нельзя было бы получить или изменить
иными способами.
Пусть функция atom принимает один аргумент, инициализирующий хранимое значение
(значение по умолчанию, в случае вызова atom без аргумента - None),
а возвращает 3 функции - get_value, set_value, process_value, delete_value,такие, что:

get_value - позволяет получить значение хранимой переменной;
set_value - позволяет установить новое значение хранимой переменной,
возвращает его;
process_value - принимает в качестве аргументов сколько угодно функций
и последовательно (в порядке перечисления аргументов) применяет эти функции
к хранимой переменной, обновляя ее значение (перезаписывая получившийся
результат) и возвращая получишееся итоговое значение.
delete_value - удаляет значение
"""


def inc(a):
    a += 1
    return a


def double(a):
    a *= 2
    return a


def atom(value=None):

    def get_value():
        return value

    def set_value(new_value):
        nonlocal value
        value = new_value
        return value

    def process_value(*args):
        nonlocal value
        for func in args:
            value = func(value)
        return value

    def delete_value():
        nonlocal value
        value = None
        return value

    return get_value, set_value, process_value, delete_value


get_v, set_v, proc_v, del_v = atom(2)

print(get_v())
set_v(3)
print(get_v())
proc_v(inc, double)
print(get_v())
del_v()
print(get_v())

