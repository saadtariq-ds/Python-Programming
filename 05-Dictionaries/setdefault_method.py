from contents_quantities import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"Chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"Beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"Ketchup: {ketchup_quantity}")

print()
print("`Pantry` now contains")

for key, value in sorted(pantry.items()):
    print(key, value)
