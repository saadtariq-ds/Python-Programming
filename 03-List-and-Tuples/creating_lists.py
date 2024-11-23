empty_list = []

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

print("--" * 20)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

print("--" * 20)

digits = sorted("432985617")
print(digits)

print("--" * 20)

digits = list("432985617")
print(digits)

print("--" * 20)

more_numbers = list(numbers)
print(numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)

print("--" * 20)

# Slicing
more_numbers = numbers[:]
print(numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)

print("--" * 20)

more_numbers = numbers.copy()
print(numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)