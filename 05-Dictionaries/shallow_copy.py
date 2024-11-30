# animals = {
#     "lion": "scary",
#     "elephant": "big",
#     "teddy": "cuddly"
# }

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}

# things = animals
# animals["teddy"] = "toy"
# print(things["teddy"])
# print(animals["teddy"])

# things = animals.copy()
# animals["teddy"] = "toy"
# print(things["teddy"])
# print(animals["teddy"])

things = animals.copy()
print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
