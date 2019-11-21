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


def atom(a=None):

    value = int(a)

    def get_value():
        nonlocal value
        return value

    def set_value(new_value=None):
        nonlocal value
        new_value = int(input('new value = '))
        value = new_value
        return value

    def process_value():
        nonlocal value
        func_str = input('write function(s) to process value (separate by space): ')
        func_list = func_str.split()
        for func in func_list:
            value = eval(func)(value)
        return value

    def delete_value():
        nonlocal value
        value = None
        return value

    while True:
        action = input('get value ------ print 1\nset new value -- print 2\n'
                       'process value -- print 3\ndelete value --- print 4\n'
                       'exit ----------- print 5\n>>> ')
        if action == '1':
            print(get_value())
        elif action == '2':
            set_value()
        elif action == '3':
            process_value()
        elif action == '4':
            delete_value()
        elif action == '5':
            break

    return value


atom(2)
