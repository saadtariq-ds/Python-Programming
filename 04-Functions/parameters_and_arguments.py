def multiply(number1, number2):
    result = number1 * number2
    return result


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for value in range(1, 5):
    two_times = multiply(2, value)
    print(two_times)
