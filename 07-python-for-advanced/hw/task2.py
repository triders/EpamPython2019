"""
Написать свое property c кэшем и таймаутом
полностью повторяет поведение стандартной property за исключением:
    * хранит результат работы метода некоторое время, которое передается
      параметром в инициализацию проперти
    * пересчитывает значение, если таймер истек
"""

import time
import uuid


def timer_property(t):
    class Property:
        time_interval = t

        def __init__(self, fget=None, fset=None, fdel=None, doc=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            if doc is None and fget is not None:
                doc = fget.__doc__
            self.__doc__ = doc
            self.value_set_time = None
            self.last_value = None

        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            if self.fget is None:
                raise AttributeError("unreadable attribute")
            if self.value_set_time is None or \
                    time.time() - self.value_set_time > Property.time_interval:
                self.last_value = self.fget(obj)
                self.value_set_time = time.time()
            return self.last_value

        def __set__(self, obj, value):
            if self.fset is None:
                raise AttributeError("can't set attribute")
            self.last_value = value
            self.value_set_time = time.time()
            self.fset(obj, value)

        def __delete__(self, obj):
            if self.fdel is None:
                raise AttributeError("can't delete attribute")
            self.fdel(obj)

        def getter(self, fget):
            return type(self)(fget, self.fset, self.fdel, self.__doc__)

        def setter(self, fset):
            return type(self)(self.fget, fset, self.fdel, self.__doc__)

        def deleter(self, fdel):
            return type(self)(self.fget, self.fset, fdel, self.__doc__)

    return Property


class Message:

    @timer_property(t=10)
    def msg(self):
        self._msg = self.get_message()
        return self._msg

    @msg.setter  # reset timer also
    def msg(self, param):
        self.msg = param

    def get_message(self):
        """
        Return random string
        """
        return uuid.uuid4().hex




if __name__ == '__main__':
    m = Message()
    initial = m.read
    assert initial is m.read
    time.sleep(10)
    assert initial is not m.read
