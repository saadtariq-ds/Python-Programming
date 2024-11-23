available_parts = ["Computer", "Monitor", "Keyboard", "Mouse",
                   "Speaker", "HDMI Cable", "DVD Drive"]

valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

current_choice = "-"
computer_parts = []     # empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # It's already in, so remove it
            print(f"Removing {current_choice}")
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {current_choice}")
            computer_parts.append(chosen_part)
        print(f"Your list now contains: {computer_parts}")
    else:
        print("Please add options from the list below")
        for index, part in enumerate(available_parts):
            print(f"{index + 1}: {part}")

    current_choice = input()

print(computer_parts)
