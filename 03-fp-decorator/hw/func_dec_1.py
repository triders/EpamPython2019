from functools import reduce

# problem 6: Sum square difference
# answer: 25164150

euler_6 = sum(range(1,101))**2 - sum([i**2 for i in range(1, 101)])
print(f'Euler 6: {euler_6}')


# problem 9: A Pythagorean triplet
# answer: 31875000, 200, 375, 425

rng = 426
euler_9 = [(a*b*c, a, b, c) for a in range(3, rng)
           for b in range(a+1, rng) for c in range(b+1, rng)
           if (a+b+c == 1000) and (a**2 + b**2 == c**2)]
print(f'Euler 9: {euler_9}')


# problem 40: Champernowne's constant
# answer: 210

seq = str([i for i in range(1, 200000)]).replace(', ', '')
euler_40 = reduce(lambda x, y: x*y, [int(seq[10**n]) for n in range(6)])

print(f'Euler 40: {euler_40}')


# problem 48: Self powers
# answer: 9110846700

euler_48 = sum([i**i for i in range(1, 1001)]) % 10**10
print(f'Euler 48: {euler_48}')
