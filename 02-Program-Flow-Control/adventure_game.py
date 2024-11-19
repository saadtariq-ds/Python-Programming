# available_exits = ['north', 'south', 'east', 'west']
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#
# print("Aren't you glad you got out of there")


available_exits = ['north', 'south', 'east', 'west']

chosen_exit = ""
while chosen_exit.casefold() not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break

print("Aren't you glad you got out of there")
