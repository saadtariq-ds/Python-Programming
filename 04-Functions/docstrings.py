import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid 'int' is entered

    :param prompt: The string that the user will see, when they're
        prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

        print(f"{temp} is not a valid number")


lowest = 1
highest = 100
answer = random.randint(lowest, highest)
guess = 0
print(f"Please guess a number between {lowest} and {highest}: ")

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        print("Game Over")
        break
    if guess == answer:
        print("You guess it correctly")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
