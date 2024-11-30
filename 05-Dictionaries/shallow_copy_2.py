lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list
}

# things = animals.copy()
# print(things["teddy"])
# print(animals["teddy"])
#
# print()
#
# things["teddy"].append("toy")
# teddy_list.append("toy")
# print(things["teddy"])
# print(animals["teddy"])

things = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

print(things["teddy"])
print(animals["teddy"])

print()

teddy_list.append("toy")
animals["teddy"].append("Added via `animal`")
things["teddy"].append("Added via `things`")
print(things["teddy"])
print(animals["teddy"])
print(teddy_list)
