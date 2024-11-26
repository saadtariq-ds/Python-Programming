def fibonacci(n):
    """
    Return the `n` th Fibonacci number, for positive `n`.

    :param n: the positive number
    :return: Fibonacci number
    """
    if 0 <= n <= 1:
        return n

    n_minus_1, n_minus_2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus_2 + n_minus_1
        n_minus_2 = n_minus_1
        n_minus_1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))
