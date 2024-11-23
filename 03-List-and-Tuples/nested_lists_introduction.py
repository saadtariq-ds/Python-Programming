empty_list = []

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number in numbers:
    print(number)
    for value in number:
        print(value)
