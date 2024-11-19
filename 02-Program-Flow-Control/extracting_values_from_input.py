number = input("Please enter series of numbers, using any separators you like: ")
separators = ""

for character in number:
    if not character.isnumeric():
        separators = separators + character

# print(separators)

values = "".join(character if character not in separators else " " for character in number).split()
print(sum([int(value) for value in values]))
