data = [
    "blue", "red", "blue", "green", "red", "blue", "white"
]

# Create a set from list, to remove duplicates.
unique_data = set(data)
print(unique_data)

# Create a list of unique colors, keeping the order appeared.
unique_data = list(dict.fromkeys(data))
print(unique_data)
