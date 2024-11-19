# Write a program to print a number of options, and allow the user to
# select an option from the list. Make sure there are atleast 4 options.

# The program should continue looping, allowing the user to choose one
# of the options each time around.

# The loop should only terminate when the user chooses 0.

# If the user make a valid choice, the program should print a short
# message and include the value they typed.


# choice = "-"
# while True:
#     if choice == '0':
#         break
#     elif choice in "12345":
#         print(f"You choose {choice}")
#     else:
#         print("Please choose your option from list below: ")
#         print("1:\tLearn Python")
#         print("2:\tLearn SQL")
#         print("3:\tLearn Machine Learning")
#         print("4:\tLearn Data Science")
#         print("5:\tLearn Data Engineering")
#         print("0:\tExit")
#
#     choice = input()


choice = "-"
while choice != "0":
    if choice in "12345":
        print(f"You choose {choice}")
    else:
        print("Please choose your option from list below: ")
        print("1:\tLearn Python")
        print("2:\tLearn SQL")
        print("3:\tLearn Machine Learning")
        print("4:\tLearn Data Science")
        print("5:\tLearn Data Engineering")
        print("0:\tExit")

    choice = input()
