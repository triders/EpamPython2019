from functools import reduce


def is_armstrong(num):

    num_list = list(map(int, set(str(num))))
    arm = reduce(lambda x,y: x+y,
                 list(map(lambda x: x**len(str(num)), num_list)))
    return arm == num


assert is_armstrong(9) == True, 'Число Армстронга'
assert is_armstrong(10) == False,  'Не число Армстронга'
assert is_armstrong(153) == True, 'Число Армстронга'
