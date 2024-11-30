from contents_quantities import recipes

def my_deepcopy(data: dict) -> dict:
    """
    Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with an Attribute Error if the values aren't
    lists or dictionaries

    :param data: The dictionary to copy.
    :return: A copy of `data`, with the values being copies of the original values.
    """
    new_dict = {}
    for key, value in data.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
