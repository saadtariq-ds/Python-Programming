age = int(input("How old are you? "))

if (age >= 16) and (age <= 65):
    print("Have a great day at work")
else:
    print("Enjoy your free time")

print("--" * 30)

if (age < 16) or (age > 65):
    print("Enjoy your free time")
else:
    print("Have a great day at work")
