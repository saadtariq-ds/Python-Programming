available_parts = ["Computer", "Monitor", "Keyboard", "Mouse",
                   "Speaker", "HDMI Cable", "DVD Drive"]

valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = "-"
computer_parts = []     # empty list

while current_choice != '0':
    if current_choice in valid_choices:
        print(f"Adding {current_choice}")
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("Please add options from the list below")
        for index, part in enumerate(available_parts):
            print(f"{index + 1}: {part}")

    current_choice = input()

print(computer_parts)
