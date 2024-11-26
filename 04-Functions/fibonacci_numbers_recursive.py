def fibonacci_recursive(n):
    """
        Return the `n` th Fibonacci number, for positive `n`.
        Using the recursive function

        :param n: the positive number
        :return: Fibonacci number
        """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


for i in range(10):
    print(i, fibonacci_recursive(i))
