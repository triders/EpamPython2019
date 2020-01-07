"""
Реализовать класс Quaternion, позволяющий работать с кватернионами
https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD
Функциональность (магическими методами):
- сложение
- умножение
- деление
- сравнение
- нахождение модуля
- строковое представление и repr
По желанию:
- взаимодействие с числами других типов
"""

class Quaternion:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        if isinstance(other, Quaternion):
            return eval(self.__class__.__name__)(self.a + other.a, self.b + other.b,
                              self.c + other.c, self.d + other.d)
        elif isinstance(other, int) or isinstance(other, float):
            return eval(self.__class__.__name__)(self.a + other, self.b, self.c, self.d)

    def __iadd__(self, other):
        if isinstance(other, Quaternion):
            self.a += other.a
            self.b += other.b
            self.c += other.c
            self.d += other.d
            return self
        elif isinstance(other, int) or isinstance(other, float):
            self.a += other
            return self

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            a1, b1, c1, d1 = self.a, self.b, self.c, self.d
            a2, b2, c2, d2 = other.a, other.b, other.c, other.d

            a = a1*a2 - b1*b2 - c1*c2 - d1*d2
            b = a1*b2 + b1*a2 + c1*d2 - d1*c2
            c = a1*c2 - b1*d2 + c1*a2 + d1*b2
            d = a1*d2 + b1*c2 - c1*b2 + d1*a2
            return eval(self.__class__.__name__)(a, b, c, d)

    def __truediv__(self, other):
        if isinstance(other, eval(self.__class__.__name__)):
            m = other.a**2 + other.b**2 + other.c**2 + other.d**2
            a1, b1, c1, d1 = self.a, self.b, self.c, self.d
            a2, b2, c2, d2 = other.a/m, -other.b/m, -other.c/m, -other.d/m

            return eval(self.__class__.__name__)(a1, b1, c1, d1) * eval(self.__class__.__name__)(a2, b2, c2, d2) 

    def __abs__(self):
        ab = (self.a**2 + self.b**2 + self.c**2 + self.d**2)**(1/2)
        ab = int(ab) if ab == int(ab) else ab
        return ab

    def __eq__(self, other):
        if isinstance(other, eval(self.__class__.__name__)):
            return [self.a, self.b, self.c, self.d] == \
                   [other.a, other.b, other.c, other.d]

    def __str__(self):
        return f'{self.a} + {self.b}i + {self.c}j + {self.d}k'

    def __repr__(self):
        return f"{self.__class__.__name__}({self.a}, {self.b}, {self.c}, {self.d})"


class NewQuaternion(Quaternion):
    pass


nq1 = NewQuaternion(1 ,2 ,3 ,4)
print (repr(nq1))

q1 = Quaternion(1, 2, 3, 4)
print(q1)  # 1 + 2i + 3j + 4k
print(repr(q1))  # Quaternion(1, 2, 3, 4)

q2 = eval(repr(q1))
print(q2)  # 1 + 2i + 3j + 4k

q3 = q1 + q2
print(q3)  # 2 + 4i + 6j + 8k

q4 = Quaternion(4, 4, 4, 4)
q4 += q1
print(q4)  # 5 + 6i + 7j + 8k

q5 = Quaternion(5, 5, 5, 5)
print(abs(q4))  # 13.19090595827292
print(abs(q5))  # 10

q6 = q1 + 1
print(q6) # 2 + 2i + 3j + 4k

print(q1 == q2)  # True
print(q1 == q4)  # False

q7 = q1 * q2
print(q7)  # -28 + 4i + 6j + 8k

q8 = q1 / q5
print(q8)  # 0.5 + 0.09999999999999999i + 0.0j + 0.2k
