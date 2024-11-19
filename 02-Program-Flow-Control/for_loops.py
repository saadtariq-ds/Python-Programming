# parrot = "Norwegian Blue"
#
# for character in parrot:
#     print(character)


# Stepping through a for loop
number = "9,223;372:036 854,775;807"
separators = ""

for character in number:
    if not character.isnumeric():
        separators = separators + character

print(separators)

values = "".join(character if character not in separators else " " for character in number).split()
print([int(value) for value in values])
