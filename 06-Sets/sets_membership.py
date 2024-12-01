choice = "-"
while choice != "0":
    # if choice in set("12345"):
    if choice in {"1", "2", "3", "4", "5"}:
        print(f"You choose {choice}")
    else:
        print("Please choose your option from below list:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tLearn C++")
        print("4:\tPlay Cricket")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()
