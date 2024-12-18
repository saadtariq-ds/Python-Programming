animals = {
    "Turtle",
    "Horse",
    "Robin",
    "Python",
    "Swallow",
    "Hedgehog",
    "Wren",
    "Aardvark",
    "Cat",
}

birds = {
    "Robin", "Swallow", "Wren"
}

print(f"Birds is a subset of animals: {birds.issubset(animals)}")
print(f"Animals is a superset of birds: {animals.issuperset(birds)}")

print(f"Birds is a superset of animals: {birds.issuperset(animals)}")
print(f"Animals is a subset of birds: {animals.issubset(birds)}")
