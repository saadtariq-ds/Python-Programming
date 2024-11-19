answer = 5

guess = int(input("Please guess a number between 1 and 10: "))

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("You guess correctly")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("You guess correctly")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You guess correctly in the first attempt")


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
