from deep_copy_challenge import my_deepcopy
import copy

original = {
    "Saad": ["Tariq", ["Programmer", "Data Scientist"]],
    "Lionel": ["Messi", ["Sportsperson", "Footballer"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

print(original)
print(copy_1)
print(copy_2)

print()

original["Saad"].append("Pakistan")
original["Lionel"].append("Argentina")

print(original)
print(copy_1)
print(copy_2)

original["Saad"][1].append("Student")
lionel_list = original["Lionel"]
lionel_list[1].append("Ballon d'or Winner")

print()

print(original)
print(copy_1)
print(copy_2)