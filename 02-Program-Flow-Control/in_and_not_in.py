parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print(f"{letter} is in {parrot}")
else:
    print(f"{letter} is not in {parrot}")

print("--" * 30)

activity = input("What would you like to do today? ")
if "cinema" not in activity.casefold():
    print("But i want to go to cinema")
