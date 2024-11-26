def multiply(x, y):
    """
    This function is used to multiple 2 numbers.

    :param x: the first number to multiply
    :param y: the second number to multiply
    :return: the product of 'x' and 'y'
    """
    result = x * y
    return result


def is_word_palindrome(word):
    """
    Check if a string is a palindrome.

    :param word: The string to check
    :return: True if 'string' is palindrome, False otherwise
    """
    word = word.casefold()
    return word[::-1] == word


def is_sentence_palindrome(sentence):
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
