def is_word_palindrome(word):
    word = word.casefold()
    return word[::-1] == word

def is_sentence_palindrome(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    string = string.casefold()
    return string[::-1] == string


# word = input("Please enter a word to check: ")
#
# if is_word_palindrome(word=word):
#     print(f"'{word}' is palindrome")
# else:
#     print(f"'{word}' is not palindrome")


sentence = input("Please enter a sentence to check: ")

if is_sentence_palindrome(sentence=sentence):
    print(f"'{sentence}' is palindrome")
else:
    print(f"'{sentence}' is not palindrome")
