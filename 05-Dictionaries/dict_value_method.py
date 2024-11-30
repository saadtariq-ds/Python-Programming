d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ["chicken", "spam", "egg", "bread", "lemon"]

values = d.values()
print(values)

d[10] = "ten"
print(values)

print()

# Checking if value exist
print("four" in values)
print("eleven" in values)

print()

# Key with the value
keys = list(d.keys())
values = list(values)
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

print()

# Key with the value
for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key {key}")
