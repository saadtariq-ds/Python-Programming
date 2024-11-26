def factorial(number: int) -> int:
    """
    Calculating factorials of a number

    :param number: the number to calculate
    :return: the factorial result of a number
    """
    if number <= 1:
        return 1

    result = 2
    for i in range(3, number + 1):
        result *= i

    return result


def factorial_recursive(number: int) -> int:
    """
    Calculating factorials of a number

    :param number: the number to calculate
    :return: the factorial result of a number
    """
    if number <= 1:
        return 1

    return number * factorial_recursive(number - 1)


for i in range(36):
    # print(i, factorial(i))
    print(i, factorial_recursive(i))
