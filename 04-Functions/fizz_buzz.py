def fizz_buzz(number: int) -> str:
    """
    Play Fizz Buzz
    :param number: the number to check
    :return: 'fizz' if the number is divisible by 3
        'buzz' if the number is divisible by 5
        'fizz buzz' if the number is divisible by both 3 and 5
        The number, as a string, otherwise
    """

    if (number % 3 == 0) and (number % 5 == 0):
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


# for i in range(1, 101):
#     print(fizz_buzz(i))

input("Play Fizz Buzz. Press ENTER to start: ")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Your go: ")
    if player_answer != correct_answer:
        print(f"You lose, the correct answer was {correct_answer}")
        break
else:
    print(f"Well done, you reached {next_number}")
