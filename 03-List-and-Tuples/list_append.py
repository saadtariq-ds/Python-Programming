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
        print("1: Computer")
        print("2: Monitor")
        print("3: Keyboard")
        print("4: Mouse")
        print("5: Speaker")
        print("6: HDMI")
        print("0: to finish")

    current_choice = input()

print(computer_parts)
