'''
DESCRIPTION:
Just like in the "father" kata, you will have to return the last digit of the nth element in the Fibonacci sequence (starting with 1,1, to be extra clear, not with 0,1 or other numbers).

You will just get much bigger numbers, so good luck bruteforcing your way through it ;)
'''


def last_fib_digit(n: int) -> int:
    a, b = 0, 1
    for _ in range(n % 60):
        a, b = b, (a+b) % 10
    return a


print(last_fib_digit(7000006))


# Another solution
def last_fib_digit1(n: int) -> int:
    return [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1][n % 60]
