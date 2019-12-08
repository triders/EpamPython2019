""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""


class Suppressor:
    def __init__(self, error_class):
        self.error_class = error_class

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is self.error_class:
            print("it's fine")
            return True

with Suppressor(ZeroDivisionError):
    n = 1/0
