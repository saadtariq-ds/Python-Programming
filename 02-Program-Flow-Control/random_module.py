import random

lowest = 1
highest = 10
answer = random.randint(lowest, highest)

guess = int(input(f"Please guess a number between {lowest} and {highest}: "))

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("You guess correctly")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You guess correctly in the first attempt")
