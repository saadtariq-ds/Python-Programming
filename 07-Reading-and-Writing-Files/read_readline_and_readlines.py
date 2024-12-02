# Read Lines
# with open(file='Jabberwocky.txt', mode='r') as jabber:
#     lines = jabber.readlines()
#
# print(lines)
#
# for line in reversed(lines):
#     print(line, end='')


# Read
# with open(file='Jabberwocky.txt', mode='r') as jabber:
#     text = jabber.read()
#
# print(text)
# for character in reversed(text):
#     print(character, end='')


# Read Line
with open(file='Jabberwocky.txt', mode='r') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if "jubjub" in line.casefold():
            break
