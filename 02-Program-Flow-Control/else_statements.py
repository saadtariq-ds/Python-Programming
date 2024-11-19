name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print(f"{name} is {age} years old")

if age >= 18:
    print(f"{name} is old enough to vote")
    print("Please put an X in the box")
else:
    print(f"{name} is not old enough to vote")
    print(f"Please come back in {18 - age} years")
