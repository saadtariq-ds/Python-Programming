day = "Saturday"
temperature = 30
raining = True

if day == "Saturday" and temperature > 27 and not raining:
    print("Go Swimming")
else:
    print("Sit at home")

print("--" * 30)

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go Swimming")
else:
    print("Sit at home")
