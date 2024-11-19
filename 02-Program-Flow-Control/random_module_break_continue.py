import random

lowest = 1
highest = 100
answer = random.randint(lowest, highest)

guess = 0
print(f"Please guess a number between {lowest} and {highest}: ")

while guess != answer:
    guess = int(input())

    if guess == 0:
        print("Game Over")
        break
    if guess == answer:
        print("You guess it correctly")
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
