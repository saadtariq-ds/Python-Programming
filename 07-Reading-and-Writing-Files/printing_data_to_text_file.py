data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

plants_filename = "flowers_print.txt"

# Writing Data
with open(file=plants_filename, mode='w') as plants:
    for plant in data:
        print(plant, file=plants)

# Reading Data from created file
plants_list = []
with open(file=plants_filename, mode='r') as plants:
    for plant in plants:
        plants_list.append(plant.rstrip())

print(plants_list)
