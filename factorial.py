from functools import reduce


def factorial(n):
    return sorted(set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n ** 0.5) + 1, 2 if n % 2 else 1) if n % i == 0)
        )
    ))