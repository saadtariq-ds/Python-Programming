computer_parts = ['computer', 'monitor', 'keyboard',
                  'mouse', 'speaker']

print(computer_parts)

# Replacing Mouse
computer_parts[3] = "trackball"
print(computer_parts)

# Replacing Slice
print(computer_parts[3:])
computer_parts[3:] = "mouse"
print(computer_parts)

computer_parts[3:] = ["mouse"]
print(computer_parts)
