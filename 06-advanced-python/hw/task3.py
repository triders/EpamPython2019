""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""


class Suppressor:
    def __init__(self, *error_class):
        self.error_class = error_class

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self.error_class)


with Suppressor(ZeroDivisionError, IndexError):
    n = 1/0

with Suppressor(ZeroDivisionError, IndexError):
    l = ['a']
    l[1] = 1

