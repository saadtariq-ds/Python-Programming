available_parts = ["Computer", "Monitor", "Keyboard", "Mouse",
                   "Speaker", "HDMI Cable"]
current_choice = "-"
computer_parts = []     # empty list

while current_choice != '0':
    if current_choice in "123456":
        print(f"Adding {current_choice}")
        if current_choice == '1':
            computer_parts.append("Computer")
        elif current_choice == '2':
            computer_parts.append("Monitor")
        elif current_choice == '3':
            computer_parts.append("Keyboard")
        elif current_choice == '4':
            computer_parts.append("Mouse")
        elif current_choice == '5':
            computer_parts.append("Speaker")
        elif current_choice == '6':
            computer_parts.append("HDMI")
    else:
        print("Please add options from the list below")
        for index, part in enumerate(available_parts):
            print(f"{index + 1}: {part}")

    current_choice = input()

print(computer_parts)
