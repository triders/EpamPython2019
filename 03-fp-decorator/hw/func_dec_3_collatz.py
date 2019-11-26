def collatz_steps(n):

    assert n > 0, 'Число должно быть положительным'
    assert type(n) == int, 'Число должно быть целым'

    if n == 2:
        return 1
    if n % 2 == 0:
        return 1 + collatz_steps(n//2)
    else:
        return 1 + collatz_steps(3*n+1)


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152
