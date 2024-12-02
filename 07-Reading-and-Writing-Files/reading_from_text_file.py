jabber = open(file="Jabberwocky.txt", mode='r')

for line in jabber:
    # print(line, end='')
    print(line.strip())

jabber.close()
