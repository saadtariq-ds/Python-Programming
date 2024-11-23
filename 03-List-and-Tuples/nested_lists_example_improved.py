menu = [
    ["egg", "bread"],
    ["egg", "bread", "sausage"],
    ["egg", "cheese"],
    ["egg", "bread", "cheese"],
    ["egg", "bread", "cheese", "sausage"],
    ["cheese", "bread", "sausage", "cheese"],
    ["cheese", "egg", "cheese", "cheese", "bread", "cheese"],
    ["cheese", "sausage", "cheese", "bread", "cheese", "tomato", "cheese"],
]

# Printing All menu after removing cheese
# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "cheese":
#             del meal[index]
#
#     print(meal)

for meal in menu:
    for item in meal:
        if item != "cheese":
            print(item, end=" ")
    print()
