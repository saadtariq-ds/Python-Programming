# trail_1 = {
#     "Bob", "Charley", "Georgia", "John"
# }
#
# trail_2 = {
#     "Anne", "Charley", "Eddie", "Georgia"
# }
#
# check_set = trail_1.intersection(trail_2)
# print(check_set)


farm_animals = {
    "sheep", "hen", "cow", "horse", "goat"
}

wild_animals = {
    "lion", "elephant", "tiger", "goat", "panther", "horse"
}

potential_rides = {
    "donkey", "horse", "camel"
}

intersection = farm_animals & wild_animals & potential_rides
print(intersection)

intersection = farm_animals.intersection(wild_animals.intersection(potential_rides))
print(intersection)

intersection = farm_animals.intersection(wild_animals, potential_rides)
print(intersection)
