name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print(f"{name} is {age} years old")

if age < 2:
    print("You are a baby")
elif age < 40:
    print("You are a young adult")
elif age < 60:
    print("You are a middle-age adult")
else:
    print("You are an old-age adult")
