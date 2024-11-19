answer = 5

guess = int(input("Please guess a number between 1 and 10: "))

if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("You guess correctly")
