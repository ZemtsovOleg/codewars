import timeit


def sum_mul(n: int, m: int) -> int | str:
    if m > 0 and n > 0:
        quantity = m // n
        last = quantity * n
        if last == m:
            last -= n
            quantity -= 1
        return (last + n) / 2 * quantity
    else:
        return 'INVALID'


def sum_mul2(n: int, m: int) -> int | str:
    if m > 0 and n > 0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'


print(sum_mul(0, 0), 'INVALID')
print(sum_mul(2, 9), 20)  # ==> 2 + 4 + 6 + 8 = 20
print(sum_mul(4, -7), 'INVALID')
print(sum_mul(3, 13))  # ==> 3 + 6 + 9 + 12 = 30
print(sum_mul(4, 123))  # ==> 4 + 8 + 12 + ... = 1860
print(sum_mul(4, -7))  # ==> "INVALID"
print(sum_mul(0, 2))
print(sum_mul(0.0, 2))
print(sum_mul(2, 10))


print(timeit.timeit(lambda: sum_mul(4, 123456), number=1000))
print(timeit.timeit(lambda: sum_mul2(4, 123456), number=1000))
