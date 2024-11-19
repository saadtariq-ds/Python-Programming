low = 1
high = 1000

print(f"Please think of a number between {low} and {high}")
input("Please ENTER to start ")

guesses = 1
while low != high:
    print(f"\tGuessing in the range of {low} and {high}")
    guess = low + (high - low) // 2
    high_low = input(f"My guess is {guess}, Should I guess higher "
                     f"or lower? Enter h or l, or c if my guess "
                     f"was correct ").casefold()

    if high_low == "h":
        # Guess Higher. The low end of the range becomes 1 greater than
        # the guess
        low = guess + 1
    elif high_low == "l":
        # Guess Lower. The high end of the range becomes 1 less than
        # the guess
        high = guess - 1
    elif high_low == "c":
        print(f"I got it in {guesses} guesses")
        break
    else:
        print("Please enter h, l, or c")

    guesses += 1
else:
    print(f"You thought of the number {low}")
    print(f"I got it in {guesses} guesses")
