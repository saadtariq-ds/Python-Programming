filename = "Jabberwocky.txt"
with open(file=filename, mode='r') as poem:
    first = poem.readline().rstrip()

print(first)

# chars = "'"
# chars = "'Twas"
chars = "' Twasebv"
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

for character in first:
    if character in chars:
        print(f"Removing {character}")
    else:
        break

print("*" * 80)

for character in first[::-1]:
    if character in chars:
        print(f"Removing {character}")
    else:
        break
