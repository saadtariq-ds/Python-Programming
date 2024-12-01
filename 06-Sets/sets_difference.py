farm_animals = {
    "sheep", "hen", "cow", "horse", "goat"
}

wild_animals = {
    "lion", "elephant", "tiger", "goat", "panther", "horse"
}

# Farm Animals - Wild Animals
print(farm_animals.difference(wild_animals))

# Wild Animals - Farm Animals
print(wild_animals.difference(farm_animals))
