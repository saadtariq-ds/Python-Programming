with open(file='Jabberwocky.txt', mode='r', encoding='utf-8') as jabber:
    for line in jabber:
        print(line.rstrip())
