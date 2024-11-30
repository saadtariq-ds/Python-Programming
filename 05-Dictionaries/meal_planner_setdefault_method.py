from contents_quantities import pantry, recipes

def add_shopping_item(data: dict, item:str, amount: int) -> None:
    """
    Add a tuple containing `item` and `amount` to the `data` dict
    :param data: dictionary of items that needs to buy
    :param item: name of item that needs to buy
    :param amount: quantity of the item
    """
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount


display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}
while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("------------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking Ingredients ....")
        ingredients = recipes[selected_item]
        print(ingredients)

        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item} ")
                add_shopping_item(
                    data=shopping_list, item=food_item, amount=quantity_to_buy)

for things in shopping_list.items():
    print(things)
