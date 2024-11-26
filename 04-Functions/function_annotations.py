def is_word_palindrome(word: str) -> bool:
    """
    Check if a string is a palindrome.

    :param word: The string to check
    :return: True if 'string' is palindrome, False otherwise
    """
    word = word.casefold()
    return word[::-1] == word


def is_sentence_palindrome(sentence: str) -> bool:
    """
    Check if a sentence is palindrome.

    The function ignores whitespaces, captialization and punctuation
    in the sentence.

    :param sentence: The sentence to check
    :return: True if 'sentence' is palindrome, False otherwise
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return is_word_palindrome(string)


def fibonacci_recursive(n: int) -> int:
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


def multiply(x: float, y: float) -> float:
    """
    This function is used to multiple 2 numbers.

    :param x: the first number to multiply
    :param y: the second number to multiply
    :return: the product of 'x' and 'y'
    """
    result = x * y
    return result

# p = is_word_palindrome()
# p = is_sentence_palindrome()
# p = fibonacci_recursive()
p = multiply()
